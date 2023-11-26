from django import forms


class MpesaPaymentForm(forms.Form):
    phone_number = forms.CharField(max_length=12, label="Phone Number")
    amount = forms.DecimalField(max_digits=10, decimal_places=2, label="Amount")
