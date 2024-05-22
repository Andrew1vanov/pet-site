import numpy as np
from plotly import graph_objects as go

def d_macd(sct):
    MACD = d_ema(sct, n = 12) - d_ema(sct, n = 26)
    SIGNAL = d_ema(MACD, n = 9)
    return MACD, SIGNAL


#Осцилляторы
def d_momentum(sct, n = 5):
    MOMENTUM = [sct[i]/sct[i - n] * 100 if i > n else 0 for i in range(len(sct))]
    return MOMENTUM

def d_rsi(sct, n = 14):
    '''Relative Strength Index'''
    RSI = []
    for i in range(n+1, len(sct)):
        g = sct[i-n:i] - sct[i-n-1:i-1]
        U = np.mean(g[np.where(g > 0)[0]])
        D = abs(np.mean(g[np.where(g < 0)[0]]))
        RSI.append(100 - (100/(1 + U/D)))
    RSI = np.asarray(RSI)
    return RSI

def d_obv(sct, vol):
    '''On Balance Volume'''
    OBV = [0]
    for i in np.arange(len(sct)):
        if sct[i]-sct[i-1] > 0:
            OBV.append(OBV[i-1] + vol[i])
        elif sct[i]-sct[i-1] == 0:
            OBV.append(OBV[i-1])
        else:
            OBV.append(OBV[i-1] - vol[i])
    OBV.pop(0)
    return OBV

def analys_plot(price: list, volume: list, dates: list = None, items = None) -> go.Figure:
    
    if not dates:
        dates = [i for i in range(len(price))]

    x_rev = dates[::-1]
    fig_price = go.Figure()
    fig_price.add_trace(go.Scatter(x = dates,y = price, mode = 'lines', name='price', showlegend=False))
    for item in items:
        line = item.plot(sct = price, vol = volume)
        fig_price.add_trace(go.Scatter(x = dates, y = line, name = item.name, line=dict(
            color = item.color, dash = item.linestyle), showlegend= False 
        ))
        if item.lineType == 'SMA' and item.period == 20:
            bb_up, bb_low = item.bollinger_bands(price, line)
            bb_low = bb_low[::-1]
            fig_price.add_trace(go.Scatter(x = dates+x_rev, 
                y = bb_up + bb_low,
                fill='toself',
                fillcolor='rgba(74, 255, 189, 0.3)',
                line_color = 'rgba(74, 255, 189, 0.5)',
                showlegend=False
                ))
    
    return fig_price