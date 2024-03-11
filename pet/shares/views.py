from django.shortcuts import render, get_object_or_404
from .moex_all import MOEX_session
from .models import Security
import plotly.graph_objects as go
from analys.forms import Bollinger_form, MovingAvr
from analys.models import MovingAverages
# Create your views here.

def title_page(request):
    securities = Security.objects.all()
    return render(request, 'shares/share/title_page.html', 
                  {'securities': securities})

def security_detail(request, slug):
    security = get_object_or_404(Security, slug = slug)
    price, volume = security.price, security.volume

    fig_price = go.Figure()
    fig_price.add_trace(go.Scatter(y = price, mode = 'lines'))
    for item in MovingAverages.objects.all():
        line = item.plot(price, volume)
        fig_price.add_trace(go.Scatter(y = line, mode = 'lines'))
    line_price = fig_price.to_html(full_html = False, include_plotlyjs = False)

    bollinger_form = Bollinger_form()
    moving_form = MovingAvr()

    return render(request, 'shares/share/security_detail.html',
                  {'security': security,
                   'line_price': line_price,
                   'form': bollinger_form,
                   'moving_form': moving_form})

def all_securities(request):
    moex_list = MOEX_session(request)
    #moex_list.securirties_update()
    return render(request, 'shares/share/all_securities.html', 
                  {'moex_list': moex_list})
