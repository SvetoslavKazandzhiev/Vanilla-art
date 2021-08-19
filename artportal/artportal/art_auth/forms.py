from django import forms
from django.contrib.auth import authenticate, get_user_model, password_validation
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError

from artportal.art_auth.models import Account

UserModel = get_user_model()


class LoginForm(forms.Form):
    user = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput(),
    )

    def clean_password(self):
        self.user = authenticate(
            username=self.cleaned_data['user'],
            password=self.cleaned_data['password'],
        )
        if not self.user:
            raise ValidationError('Username name or password incorrect')

    def save(self):
        return self.user


class RegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username',)
        help_text = password_validation.password_validators_help_text_html()


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('profile_image',)
