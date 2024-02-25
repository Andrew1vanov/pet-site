from django.urls import path
from . import views

app_name = 'shares'

urlpatterns = [
    path('', views.title_page, name = 'title_page'),
    path('<int:id>/<slug:slug>/', views.security_detail, name = 'security_detail'),
    path('securities/', views.all_securitites, name = 'all_security_list'),
]