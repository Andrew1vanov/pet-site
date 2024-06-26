from django.shortcuts import render, get_object_or_404
from .moex_all import MOEX_session
from .models import Security
from analys.forms import MovingAveragesForm
from analys.models import MovingAverages
from analys.analys import analys_plot
from django.core.cache import cache
# Create your views here.

def title_page(request):
    securities = Security.objects.all()
    return render(request, 'shares/share/title_page.html', 
                  {'securities': securities})

def security_detail(request, slug) -> render:
    key = f'{slug}'
    security = cache.get(key)
    if not security:
        security = get_object_or_404(Security, slug = slug)
        cache.set(key, security)
   
    price, volume = security.price_all, security.volume
    dates = security.trade_dates
    fig_price = analys_plot(price, volume, dates = dates,items = MovingAverages.objects.all())
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
