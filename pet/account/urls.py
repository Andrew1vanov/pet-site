from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.AccountRegistration.as_view(),
         name = 'investor_registration'),
    path('login/', views.AccountLogin.as_view(), name = 'login'),
    path('logout/', views.logout_view, name = 'logout'),    
    path('update/', views.AccountChangeView.as_view(), name = 'account_update'),
    path('', views.accuont_view, name='account_view'),
]