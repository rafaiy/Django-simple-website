from django.contrib.auth.models import user_logged_in
from django.contrib.auth.models import User
from django.forms import ModelForm,PasswordInput,CharField
from django import forms

class Userform(ModelForm):
    password = CharField(widget=PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


