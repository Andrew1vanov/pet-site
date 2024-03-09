from django import forms

class Bollinger_form(forms.Form):
    period = forms.BooleanField(required= True, 
                                initial= False,)
    abee = forms.IntegerField(min_value= 0, max_value= 500)

class MovingAvr(forms.Form):
    sma = forms.IntegerField()