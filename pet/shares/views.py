from django.shortcuts import render, get_object_or_404
from .moex_all import MOEX_all
from .models import Security
# Create your views here.

def title_page(request):
    securities = Security.objects.all()
    return render(request, 'shares/share/title_page.html', 
                  {'securities': securities})

def security_detail(request, id, slug):
    security = get_object_or_404(Security, id = id, slug = slug)
    return render(request, 'shares/share/security_detail.html',
                  {'security': security})

def all_securitites(request):
    moex_list = MOEX_all(request)
    return render(request, 'shares/share/all_securities.html', 
                  {'moex_list': moex_list})