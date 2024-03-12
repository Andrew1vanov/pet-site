from django import forms

class Bollinger_form(forms.Form):
    period = forms.BooleanField(required= False, 
                                initial= False,)


class MovingAveragesForm(forms.Form):
    period = forms.IntegerField()
    line_type = forms.ChoiceField(choices= [('SMA', 'SMA'), ('WMA', 'WMA'), ('EMA', 'EMA')])
