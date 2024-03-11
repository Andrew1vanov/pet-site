from django import forms

class Bollinger_form(forms.Form):
    period = forms.BooleanField(required= False, 
                                initial= False,)

class EMA_form(forms.Form):
    EMA = forms.IntegerField()

class SMA_form(forms.Form):
    SMA = forms.IntegerField()

class WMA_form(forms.Form):
    WMA = forms.IntegerField()