from django import forms

class Form_feedback(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    feedback = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 30}))
