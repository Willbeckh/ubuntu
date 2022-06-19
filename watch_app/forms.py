from django import forms
from django.contrib.auth.models import User


# user form
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
