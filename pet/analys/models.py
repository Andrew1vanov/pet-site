from django.db import models
from django.contrib.postgres.fields import ArrayField
import numpy as np
# Create your models here.

class MovingAverages(models.Model):
    name = models.CharField(max_length = 10)
    period = models.PositiveIntegerField()
    #styles ['solid', 'dot', 'dash', 'longdash', 'dashdot', 'longdashdot']
    linestyle = models.CharField(max_length = 20)
    color = models.CharField(max_length = 7)
    lineType = models.CharField(max_length = 3)

    def plot(self, sct, vol = None):
        n = self.period
        if self.lineType == 'EMA':
            K = 2/(n + 1)
            EMA = [sct[0]]
            for i in range(len(sct)):
                EMA.append(EMA[-1] + (K * (sct[i] - EMA[-1])))
            EMA.pop(0)
            return EMA
        elif self.lineType == 'SMA':
            SMA = np.array([sum(sct[i-n:i]) / n if i>=n else sct[i] for i in range(len(sct))])
            return SMA
        elif self.lineType == 'WMA':
            vol = np.asarray(vol)
            sct = np.asarray(sct)
            WMA = np.array([(sum(sct[i-n:i] * vol[i-n:i]) / sum(vol[i-n:i])) if i>=n else sct[i]
                    for i in range(len(sct))])
            return WMA
    
    def bollinger_bands(self, sct, sma):

        n = self.period
        p = len(sma)
        s = np.array([(1/n * sum((sct[i-n:i] - sma[i])**2))**(1/2) if i>=n else 0\
                        for i in range(p)])
        s = s * 2
        bb_upper = [sma[i] + s[i] for i in range(p)]
        bb_lower = [sma[i] - s[i] for i in range(p)]
        return bb_upper, bb_lower
