from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from django.forms import ModelForm
from .models import Task
import datetime


# - Create/Register a user (Model Form)
class CreateUserForm(UserCreationForm):
    
    class Meta:
        
        model = User
        fields = ['username', 'email', 'password1', 'password2','is_staff']
        exclude = ['id',]
        
# - Authentification a user (Model Form)

class LoginForm(AuthenticationForm):
    
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
    
#Create Task

class CreateTask(forms.ModelForm):
    class Meta:
        model=Task
        fields=['title','content',]
        exclude=['user',]