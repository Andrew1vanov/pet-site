from datetime import datetime
from django.conf import settings
from django.core.management.base import BaseCommand, CommandParser
from django.utils import timezone
import requests, apimoex
from ...models import Security
import pandas as pd

class Command(BaseCommand):
    help = 'Update shares data every day'

    def add_arguments(self, parser: CommandParser) -> None:
         return super().add_arguments(parser)
    
    def handle(self, *args, **options) -> None:
         
        moex_all = self.loadAllSecurities()

        for key, val in moex_all.items():
            if val['board'] == 'TQBR':
                price_s, volume_s, date_s = self.get_history(key, val['board'])
                Security.objects.create(
                    name = val['name'],
                    short_name = val['short_name'],
                    sec_id = key,
                    board = val['board'],
                    slug = str(key), 
                    trade_dates = date_s,
                    price_all = price_s,
                    volume = volume_s
                )
    
    def loadAllSecurities(self) -> dict:
        moex_all = {}
        for i in range(2):        
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

    def get_history(self, sec_id, board):
            sec = apimoex.get_board_history(
                requests.Session(), 
                security=sec_id, 
                columns= ['TRADEDATE', 'CLOSE', 'VOLUME'],
                board= board
                )
            sec = pd.DataFrame(sec)
            
            tDate = sec.iloc[:, 0].values.ravel()
            price = sec.iloc[:, 1].ffill().values.ravel()
            volume = sec.iloc[:, 2].ffill().values.ravel()
           
            tDate = [datetime.strptime(t, '%Y-%m-%d') for t in tDate]    
            price = list(price.flatten())   
            volume = list(volume.flatten())

            return price, volume, tDate