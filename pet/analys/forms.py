from django import forms

class Bollinger_form(forms.Form):
    period = forms.BooleanField(required= False, 
                                initial= False,)

class MovingAvr(forms.Form):
    EMA = forms.IntegerField()