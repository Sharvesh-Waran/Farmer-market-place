from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth.models import User
from .models import Role, UserProfile


class SignupForm(UserCreationForm):
    role = forms.ModelChoiceField(queryset=Role.objects.all(), required=True, label='Role')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'role')

    username = forms.CharField(widget=forms.TextInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    def save(self, commit=True):
        user = super().save(commit=commit)
        role = self.cleaned_data['role']
        if commit:
            UserProfile.objects.create(user=user, role=role)
        return user

class LoginForm(AuthenticationForm):
        
    username = forms.CharField(widget=forms.TextInput())

    password= forms.CharField(widget=forms.PasswordInput())