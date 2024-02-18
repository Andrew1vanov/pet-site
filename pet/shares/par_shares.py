import requests
import pandas as pd
import numpy as np

def load_shares_list():
    '''Загрузка всех инструментов MOEX биржы'''
    shares_names = np.array([])
    shares_short_names = np.array([])
    for i in range(12):        
        i = str(i*100)
        url = 'https://iss.moex.com//iss/securities.json?group_by=group&group_by_filter=stock_shares&start=%s' %i

        s = requests.get(url).json()
        #s_name = s['securities']['columns']
        s = pd.DataFrame(s['securities']['data'])
        s_names, s_short_names = s.iloc[:, 1].values.ravel(), s.iloc[:, 2].values.ravel()
        shares_names = np.append(shares_names, s_names)
        shares_short_names = np.append(shares_short_names, s_short_names)

    return shares_names, shares_short_names

