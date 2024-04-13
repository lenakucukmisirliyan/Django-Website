from django import forms
from django.contrib.auth.models import User

from .models import Product

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'image']
