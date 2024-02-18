from django.shortcuts import render
from .par_shares import load_shares_list
# Create your views here.

def title_page(request):
    names, shorts = load_shares_list()
    return render(request, 'shares/title_page.html', 
                  {'names': names,
                   'short_names': shorts})