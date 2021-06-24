from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django_countries.fields import CountryField

from django_countries import countries
COUNTRY_CHOICES = tuple(countries)


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='Last Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name')
    email = forms.EmailField(max_length=150, help_text='Email')
    age = forms.IntegerField(help_text='Age')
    country = forms.ChoiceField(choices=COUNTRY_CHOICES, required=True)
    #country = forms.CharField(max_length=2, help_text="Country")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'age', 'country', 'email', 'password1', 'password2',)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
