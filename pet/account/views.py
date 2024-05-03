from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.

def accuont_view(request):
    return render(request, 'account/acc.html')

class AccountRegistration(CreateView):
    template_name = 'account/registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('account_view')
    
    def form_valid(self, form):
        result = super().form_valid(form)
        cd = form.cleaned_data
        user = authenticate(username = cd['username'],
                            password = cd['password'])
        login(self.request, user)
        return result