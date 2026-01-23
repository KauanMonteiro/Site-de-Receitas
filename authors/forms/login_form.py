from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from utils.django_forms import add_placeholder,strong_password


class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Type your username')
        add_placeholder(self.fields['password'], 'Type your password')

    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput()
    )
