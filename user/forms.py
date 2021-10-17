from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm

# First Login Form
from django.contrib.auth.models import User


# User Login Form
class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'username', 'id': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': '', 'id': 'password'}
    ))


# Registration Form
class RegistrationForm(UserCreationForm):
    """
    This form is for creating new user in database
    """
    username = forms.CharField(required=True, max_length=15,
                               widget=forms.TextInput(
                                   attrs={
                                       "placeholder": "Username",
                                       "class": "form-control"
                                   }
                               ))
    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(
                                 attrs={
                                     "placeholder": "Email",
                                     "class": "form-control"
                                 }
                             ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class MyPasswordChangeForm(PasswordChangeForm):
    """
    Custom password change form of django
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["old_password"].widget = forms.PasswordInput(attrs={"class": "form-control"})
        self.fields["new_password1"].widget = forms.PasswordInput(attrs={"class": "form-control"})
        self.fields["new_password2"].widget = forms.PasswordInput(attrs={"class": "form-control"})

