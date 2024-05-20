from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from .forms import MyUserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def accuont_view(request):
    return render(request, 'account/acc.html')

def logout_view(request):
    logout(request)
    return redirect('/')

class AccountRegistration(CreateView):
    template_name = 'account/registration.html'
    form_class = MyUserCreationForm
    success_url = reverse_lazy('account_view')
    
    def form_valid(self, form):
        result = super().form_valid(form)
        cd = form.cleaned_data
        user = authenticate(username = cd['username'],
                            password = cd['password1'])
        login(self.request, user)
        return result

class AccountLogin(LoginView):
    template_name = 'account/login.html'
    authentication_form = AuthenticationForm
    next_page = reverse_lazy('account_view')


class AccountChangeView(CreateView):
    template_name = 'account/account_update.html'
    form_class = UserChangeForm
    success_url = reverse_lazy('account_view')

