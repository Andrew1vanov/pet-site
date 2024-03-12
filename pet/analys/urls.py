from django.urls import path
from . import views

app_name = 'analys'

urlpatterns = [
    path('add/<int:sec_id>/', views.add_bollinger, name='add_bollinger'),
    path('add_mov_aver/<int:sec_id>/', views.add_moving_averages, name = 'add_moving_averages')
]