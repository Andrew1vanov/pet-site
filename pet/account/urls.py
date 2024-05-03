from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'account'

urlpatterns = [
    path('registration/', views.AccountRegistration.as_view(),
         name = 'investor_registration'),
    path('', views.accuont_view, name='account_view'),
    #path('', include('django.contrib.auth.urls')),
]