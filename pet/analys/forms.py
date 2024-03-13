from django import forms

class MovingAveragesForm(forms.Form):
    period = forms.IntegerField()
    line_type = forms.ChoiceField(choices= [('SMA', 'SMA'), ('WMA', 'WMA'), ('EMA', 'EMA')])
