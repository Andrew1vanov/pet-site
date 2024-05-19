from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('registration/', views.AccountRegistration.as_view(),
         name = 'investor_registration'),
    path('login/', views.AccountLogin.as_view(), name = 'login'),
    path('logout/', views.logout_view, name = 'logout'),    
    path('', views.accuont_view, name='account_view'),

    #path('', include('django.contrib.auth.urls')),

]