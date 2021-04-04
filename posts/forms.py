from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )


class Create_Post(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['like','author','view']


class Create_Person(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        exclude =['user']

