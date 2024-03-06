from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _


class SignupForm(UserCreationForm):
    

      image = forms.ImageField(label=_('Profile Image'))

class Meta:
        model = UserProfile
        fields = ['username', 'first_name', 'last_name', 'email', 'image', 'user_type', 'session_type', 'password1', 'password2']
