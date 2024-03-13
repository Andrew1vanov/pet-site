from django.shortcuts import render, get_object_or_404
from .moex_all import MOEX_session
from .models import Security
import plotly.graph_objects as go
import numpy as np
from analys.forms import MovingAveragesForm
from analys.models import MovingAverages
# Create your views here.

def title_page(request):
    securities = Security.objects.all()
    return render(request, 'shares/share/title_page.html', 
                  {'securities': securities})

def security_detail(request, slug):
    security = get_object_or_404(Security, slug = slug)
    price, volume = security.price, security.volume
    x = [i for i in range(len(price))]
    x_rev = x[::-1]
    fig_price = go.Figure()
    fig_price.add_trace(go.Scatter(y = price, mode = 'lines', name='price', showlegend=False))
    for item in MovingAverages.objects.all():
        line = item.plot(sct = price, vol = volume)
        fig_price.add_trace(go.Scatter(y = line, name = item.name, line=dict(
            color = item.color, dash = item.linestyle), showlegend= False 
        ))
        if item.lineType == 'SMA' and item.period == 20:
            bb_up, bb_low = item.bollinger_bands(price, line)
            bb_low = bb_low[::-1]
            fig_price.add_trace(go.Scatter(x = x+x_rev, 
                y = bb_up + bb_low,
                fill='toself',
                fillcolor='rgba(74, 255, 189, 0.3)',
                line_color = 'rgba(74, 255, 189, 0.5)',
                showlegend=False
                ))
    
    
    
    line_price = fig_price.to_html(full_html = False, include_plotlyjs = False)

    moving_form = MovingAveragesForm()

    return render(request, 'shares/share/security_detail.html',
                  {'security': security,
                   'line_price': line_price,
                   'moving_form': moving_form})

def all_securities(request):
    moex_list = MOEX_session(request)
    #moex_list.securirties_update()
    return render(request, 'shares/share/all_securities.html', 
                  {'moex_list': moex_list})
