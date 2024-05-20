from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.urls import reverse
from django.conf import settings
import apimoex, requests
import pandas as pd

# Create your models here.

class Security(models.Model):
    name = models.CharField(max_length = 300)
    short_name = models.CharField(max_length = 100)
    sec_id = models.CharField(max_length = 10)
    board = models.CharField(max_length = 4)
    slug = models.SlugField(max_length = 120)
    description = models.TextField(blank = True)

    trade_dates = ArrayField(models.DateField())
    price_all = ArrayField(models.FloatField())
    price_year = ArrayField(models.FloatField())
    volume = ArrayField(models.BigIntegerField())

    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, 
            related_name= 'securities_liked',
            blank = True)

    class Meta:
        indexes = [models.Index(fields = ['name']), 
                   models.Index(fields = ['id', 'slug'])]
        ordering = ['short_name']
        verbose_name = 'security'
        verbose_name_plural = 'securities'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shares:security_detail', args = [self.slug])
    
    def get_history(self):
        sec = apimoex.get_board_history(
            requests.Session(), 
            security=self.sec_id, 
            columns= ['CLOSE', 'VOLUME'],
            board= self.board
            )
        sec = pd.DataFrame(sec)
        price = sec.fillna(sec.mean()).iloc[:, 0].values.ravel()
        volume = sec.fillna(sec.mean()).iloc[:, 1].values.ravel()
        price = [p for p in price]
        volume = [v for v in volume]
        return price, volume
    
