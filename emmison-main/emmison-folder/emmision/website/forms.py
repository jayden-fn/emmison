from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import user 

from django import forms
from django.forms.widgets import PasswordInput, TextInput

# register or create user form
class EmmisonUserCreationForm(UserCreationForm):

    class Meta:
        model = user
        fields = ['username', 'password1', 'password2']

# login form
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())