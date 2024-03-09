from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shares.models import Security
from .forms import Bollinger_form
# Create your views here.

@require_POST
def add_bollinger(request, sec_id):
    security = get_object_or_404(Security, id = sec_id)
    form = Bollinger_form(request.POST)
    return redirect('shares:security_detail')