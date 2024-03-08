from django.shortcuts import render

# Create your views here.

def accuont_view(request):
    return render(request, 'account/acc.html')