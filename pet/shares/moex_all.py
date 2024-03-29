from django.conf import settings
from django.urls import reverse
import requests, apimoex
import pandas as pd
import numpy as np
from .models import Security

class MOEX_session:
    def __init__(self, request):
        self.session = request.session
        moex_all = self.session.get(settings.MOEX_ALL_SESSION_ID)

        if not moex_all:
            moex_all = self.session[settings.MOEX_ALL_SESSION_ID] = self.load_moex_shares_list()
        
        self.moex_all = moex_all
    
    def load_moex_shares_list(self):
        moex_all = {}
        for i in range(25):        
            i = str(i*100)
            url = 'https://iss.moex.com//iss/securities.json?group_by=group&group_by_filter=stock_shares&start=%s' %i

            s = requests.get(url).json()
            s = pd.DataFrame(s['securities']['data'])
            s_secid, s_short_names = s.iloc[:, 1].values.ravel(), s.iloc[:, 2].values.ravel()
            s_board = s.iloc[:, 14].values.ravel()
            s_name = s.iloc[:, 4].values.ravel()
        
            for id, s_name, name, board in zip(s_secid, s_short_names, s_name, s_board):
                moex_all[id] = {'short_name': s_name, 'name': name, 'board': board}
                    
        return moex_all
    
    def __iter__(self):
        moex_all = self.moex_all.copy()

        for key, item in moex_all.items():
            item['secid'] = str(key)
            yield item

    def securirties_update(self):
        def get_history(sec_id, board):
            sec = apimoex.get_board_history(
                requests.Session(), 
                security=sec_id, 
                columns= ['CLOSE', 'VOLUME'],
                board= board
                )
            sec = pd.DataFrame(sec)
            price = sec.fillna(sec.mean()).iloc[:, 0].values.ravel()
            volume = sec.fillna(sec.mean()).iloc[:, 1].values.ravel()
            price = [p for p in price]
            volume = [v for v in volume]
            return price, volume
        
        for key, val in self.moex_all.items():
            if val['board'] == 'TQBR':
                price_s, volume_s = get_history(key, val['board'])
                Security.objects.create(
                    name = val['name'],
                    short_name = val['short_name'],
                    sec_id = key,
                    board = val['board'],
                    slug = str(key), 
                    price = price_s,
                    volume = volume_s
                )
            
    def clear(self):
        del self.session[settings.MOEX_ALL_SESSION_ID]