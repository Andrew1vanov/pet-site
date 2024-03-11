from django.urls import path
from . import views

app_name = 'analys'

urlpatterns = [
    path('add/<int:sec_id>/', views.add_bollinger, name='add_bollinger'),
    path('ema/<int:sec_id>/', views.add_EMA, name = 'add_EMA'),
    path('sma/<int:sec_id>/', views.add_SMA, name = 'add_SMA'),
    path('wma/<int:sec_id>/', views.add_WMA, name = 'add_WMA')
]