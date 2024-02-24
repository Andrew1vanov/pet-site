from django.shortcuts import render
from .par_shares import load_shares_list
from .moex_all import MOEX_all
# Create your views here.

def title_page(request):
    moex_list = MOEX_all(request)
    return render(request, 'shares/title_page.html', 
                  {'moex_list': moex_list})