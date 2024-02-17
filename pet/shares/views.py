from django.shortcuts import render

# Create your views here.

def title_page(request):
    return render(request, 'shares/title_page.html')