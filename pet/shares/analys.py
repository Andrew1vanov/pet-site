import numpy as np

def d_sma(sct, n = 21):
    SMA = np.array([sum(sct[i-n:i]) / n if i>=n else sct[i] for i in range(len(sct))])
    return SMA

def d_wma(sct, vol, n = 21):
    WMA = np.array([(sum(sct[i-n:i] * vol[i-n:i]) / sum(vol[i-n:i])) if i>=n else sct[i]
                    for i in range(len(sct))])
    return WMA

def d_ema(sct, n = 21):
    K = 2/(n+1)
    EMA = [sct[0]]
    for i in range(len(sct)):
        EMA.append(EMA[-1] + (K * (sct[i] - EMA[-1])))
    EMA.pop(0)
    EMA = np.asarray(EMA)
    return EMA

def d_Bollinger_Bands(sma):
    U_L = np.array([[(1 + 10/100) * sma[i] for i in range(len(sma))],
                    [(1 - 10/100) * sma[i] for i in range(len(sma))]])
    return U_L

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