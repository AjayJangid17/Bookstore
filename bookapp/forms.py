from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Pd,Nonfiction,Mysteries,Romance,Biography
from django.contrib.auth.models import User
from django.forms import TextInput


class UserRegistration(UserCreationForm):

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class LoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class PdForm(forms.ModelForm):

    class Meta:
        model = Pd
        fields = ('author','bookname','text','published_date')
        widgets = {'bookname' : TextInput(attrs={'class': 'input', 'placeholder': 'Book Name'})}
        # widgets = {'published_date': }

class Nonfiction_Form(forms.ModelForm):

    class Meta:
        model = Nonfiction
        fields = ('author','bookname','text','published_date')
        widgets = {'bookname' : TextInput(attrs={'class': 'input', 'placeholder': 'Book Name'})}

class Mystery_Form(forms.ModelForm):

    class Meta:
        model = Mysteries
        fields = ('author','bookname','text','published_date')
        widgets = {'bookname' : TextInput(attrs={'class': 'input', 'placeholder': 'Book Name'})}

class Romance_Form(forms.ModelForm):

    class Meta:
        model = Romance
        fields = ('author','bookname','text','published_date')
        widgets = {'bookname' : TextInput(attrs={'class': 'input', 'placeholder': 'Book Name'})}

class Biography_Form(forms.ModelForm):

    class Meta:
        model = Biography
        fields = ('author','bookname','text','published_date')
        widgets = {'bookname' : TextInput(attrs={'class': 'input', 'placeholder': 'Book Name'})}