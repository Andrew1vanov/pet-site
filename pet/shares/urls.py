from django.urls import path

from . import views

app_name = 'shares'

urlpatterns = [
    path('', views.title_page, name = 'title_page'),
    path('securities/', views.all_securities, name = 'all_security_list'),
    path('<slug:slug>/', views.security_detail, name = 'security_detail'),
    
]