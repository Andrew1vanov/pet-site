from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django import forms

class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email
    
    def clean(self) -> dict[str, Any]:
        return super().clean()

    
