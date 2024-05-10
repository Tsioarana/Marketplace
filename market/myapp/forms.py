from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import Profile
# forms.py

from django.contrib.auth.forms import PasswordResetForm

class CustomPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in ['email']:
            self.fields[fieldname].widget.attrs.update({
                'class': 'form-control',
                'placeholder': 'Enter your email',
            })


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': ' ',
            'class': 'form-control'
        })
        self.fields['password'].widget.attrs.update({
            'placeholder': ' ',
            'class': 'form-control'
        })



class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': ' ',
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': ' ',
                'class': 'form-control'
            }),
            'password1': forms.PasswordInput(attrs={
                'placeholder': ' ',
                'class': 'form-control'
            }),
            'password2': forms.PasswordInput(attrs={
                'placeholder': ' ',
                'class': 'form-control'
            }),
        }
class ChangePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in ['old_password', 'new_password1', 'new_password2']:
            self.fields[fieldname].widget.attrs.update({
                'class': 'form-control',
                'placeholder': '',
            })
class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': '',
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': '',
                'class': 'form-control'
            }),
        }
