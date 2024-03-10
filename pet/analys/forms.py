from django import forms

class Bollinger_form(forms.Form):
    period = forms.BooleanField(required= False, 
                                initial= False,)

class MovingAvr(forms.Form):
    SMA = forms.IntegerField()
    WMA = forms.IntegerField()
    EMA = forms.IntegerField()