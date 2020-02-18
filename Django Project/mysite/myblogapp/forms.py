from django import forms

class commentForm(forms.Form):
    comment = forms.CharField(label='comment', max_length=100)