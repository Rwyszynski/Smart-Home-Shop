from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from accounts.models import Client


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class AddressForm(forms.ModelForm):
    class Meta:
        model = Client
        exclude = ['user']

    address = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your address',
            'class': 'form-control',
        })
    )
