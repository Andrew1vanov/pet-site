from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('account/', views.accuont_view, name='account_view'),
]