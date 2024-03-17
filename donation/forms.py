

from django import forms

class DonationForm(forms.Form):
    amount = forms.DecimalField(label='Amount', min_value=1.00)
