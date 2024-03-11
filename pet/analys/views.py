from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shares.models import Security
from .models import MovingAverages
from .forms import Bollinger_form, EMA_form, SMA_form, WMA_form
# Create your views here.

@require_POST
def add_bollinger(request, sec_id):
    security = get_object_or_404(Security, id = sec_id)
    form = Bollinger_form(request.POST)
    return redirect('shares:security_detail', slug = security.slug)

@require_POST
def add_EMA(request, sec_id):
    security = get_object_or_404(Security, id = sec_id)
    form = EMA_form(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        MovingAverages.objects.create(
            name = f"EMA{cd['EMA']}",
            period = cd['EMA'],
            linestyle = 'dot',
            color = 'red',
            lineType = 'EMA'
        )
    return redirect('shares:security_detail', slug = security.slug)

@require_POST
def add_SMA(request, sec_id):
    security = get_object_or_404(Security, id = sec_id)
    form = SMA_form(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        MovingAverages.objects.create(
            name = f"SMA{cd['SMA']}",
            period = cd['SMA'],
            linestyle = 'dash',
            color = 'yellow',
            lineType = 'SMA'
        )
    return redirect('shares:security_detail', slug = security.slug)

@require_POST
def add_WMA(request, sec_id):
    security = get_object_or_404(Security, id = sec_id)
    form = WMA_form(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        MovingAverages.objects.create(
            name = f"WMA{cd['WMA']}",
            period = cd['WMA'],
            linestyle = 'dashdot',
            color = 'orange',
            lineType = 'WMA'
        )
    return redirect('shares:security_detail', slug = security.slug)