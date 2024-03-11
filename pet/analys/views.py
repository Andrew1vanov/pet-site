from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shares.models import Security
from .models import MovingAverages
from .forms import Bollinger_form, MovingAvr
# Create your views here.

@require_POST
def add_bollinger(request, sec_id):
    security = get_object_or_404(Security, id = sec_id)
    form = Bollinger_form(request.POST)
    return redirect('shares:security_detail', slug = security.slug)

@require_POST
def add_moving_average(request, sec_id):
    security = get_object_or_404(Security, id = sec_id)
    form = MovingAvr(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        MovingAverages.objects.create(
            name = f"EMA{cd['EMA']}",
            period = cd['EMA'],
            linestyle = 'dotted',
            color = 'red',
            lineType = 'EMA'
        )
    else: print('No valid')
    return redirect('shares:security_detail', slug = security.slug)
