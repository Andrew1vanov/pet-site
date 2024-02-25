from django.conf import settings
from django.urls import reverse
import requests
import pandas as pd
import numpy as np

class MOEX_all:
    def __init__(self, request):
        self.session = request.session
        moex_all = self.session.get(settings.MOEX_ALL_SESSION_ID)

        if not moex_all:
            moex_all = self.session[settings.MOEX_ALL_SESSION_ID] = self.load_moex_shares_list()
        
        self.moex_all = moex_all
    
    def load_moex_shares_list(self):
        moex_all = {}
        for i in range(12):        
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
