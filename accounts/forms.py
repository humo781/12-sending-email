from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        # for field in self.fields:
        #     self.fields[field].help_text = None
        self.fields['username'].help_text = None

    password1 = forms.CharField(
        label="Parol kiriting",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )
    password2 = forms.CharField(
        label="Parolni qayta kiriting",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email')
        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'email': forms.EmailInput(
                attrs={'class': 'form-control'}
            ),
        }


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=25,
        label='Foydalanuvchi nomi',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        label='Parol',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
