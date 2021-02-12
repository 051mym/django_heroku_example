from django import forms
from myapp.models import Dreamreal

class LoginForm(forms.Form):
   username = forms.CharField(max_length = 100,widget=forms.TextInput(attrs={'placeholder': 'Username'}))
   password = forms.CharField(widget = forms.PasswordInput())

class ProfileForm(forms.Form):
   name = forms.CharField(max_length = 100)
   picture = forms.ImageField()