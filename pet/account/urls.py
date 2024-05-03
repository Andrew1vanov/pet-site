from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'account'

urlpatterns = [
    path('', views.accuont_view, name='account_view'),
    path('registration/', views.InvestorRegistration.as_view(),
         name = 'investor_registration'),
    path('', include('django.contrib.auth.urls')),
]