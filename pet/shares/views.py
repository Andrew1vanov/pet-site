from django.shortcuts import render, get_object_or_404
from .moex_all import MOEX_all
from .models import Security
import plotly.express as px
# Create your views here.

def title_page(request):
    securities = Security.objects.all()
    return render(request, 'shares/share/title_page.html', 
                  {'securities': securities})

def security_detail(request, id, slug):
    security = get_object_or_404(Security, id = id, slug = slug)
    price, volume = security.get_history()

    fig_price = px.line(y=price)
    line_price = fig_price.to_html(full_html = False, include_plotlyjs = False)

    return render(request, 'shares/share/security_detail.html',
                  {'security': security,
                   'line_price': line_price})

def all_securitites(request):
    moex_list = MOEX_all(request)
    return render(request, 'shares/share/all_securities.html', 
                  {'moex_list': moex_list})