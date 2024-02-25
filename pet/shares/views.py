from django.shortcuts import render
from .moex_all import MOEX_all
# Create your views here.

def title_page(request):
    moex_list = MOEX_all(request)
    return render(request, 'shares/share/title_page.html', 
                  {'moex_list': moex_list})

def security_detail(request):
    
    return render(request, 'shares/share/security_detail.html')

def all_securitites(request):
    moex_list = MOEX_all(request)
    return render(request, 'shares/share/all_securities.html', 
                  {'moex_list': moex_list})