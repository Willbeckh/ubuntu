from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# app imports
from watch_app.models import Post


# user form
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', ]

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name..'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name..'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email...'}),
        }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name....'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name..'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username..'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email...'}),
        }


# post form
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'picture']
