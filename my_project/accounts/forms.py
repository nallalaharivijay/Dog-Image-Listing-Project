# forms.py

from django import forms

class SearchForm(forms.Form):
    response_code = forms.CharField(
        required=True,
        label="Response Code",
        widget=forms.TextInput(attrs={'placeholder': 'Enter response code or pattern like 2xx, 20x, etc.'})
    )
