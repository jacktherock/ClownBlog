from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.forms import fields, widgets
from django.utils.translation import gettext, gettext_lazy as _
from .models import Contact, Post
from tinymce.widgets import TinyMCE

# SignUp Form - create new user  
class SignupForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label= 'Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label= 'Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email':'Email'}

# Login Form - login new created user 
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'password']

# Contact Form - adding new sended contacts in Contact model
class ContactForm(forms.ModelForm):
    name = forms.CharField(required=False, widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}),)
    address = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Contact
        fields = ['name', 'email', 'address', 'message']
        widgets = {
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'message':forms.Textarea(attrs={'class':'form-control'}),
        }

# Post Form - adding new posts in Post model
class PostForm(forms.ModelForm):
    # description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    class Meta:
        model = Post
        fields = ['title', 'description']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            }

class EditUserDetailForm(UserChangeForm):
    password = None
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(required=False, label='First Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(required=False, label='Last Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email':'Email'}