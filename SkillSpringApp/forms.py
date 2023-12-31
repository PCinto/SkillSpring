from django import forms
from SkillSpringApp.models import Products
from SkillSpringApp import views


class MpesaPaymentForm(forms.Form):
    phone_number = forms.CharField(max_length=12, label="Phone Number")
    amount = forms.DecimalField(max_digits=10, decimal_places=2, label="Amount")

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'course', 'phone', 'email', 'origin', 'time']
