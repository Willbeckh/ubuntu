from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# user form
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', ]

        widgets = {
            'first_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name..'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name..'}),
            'email' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email...'}),
        }
        
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username..'}),
            'email' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email...'}),
        }