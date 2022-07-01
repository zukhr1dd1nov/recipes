from django import forms
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
import re
from django.utils.translation import gettext_lazy as _


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    confirm = forms.CharField(max_length=10, required=True, label=_("Parol takroran"),min_length=8, widget=forms.PasswordInput())
    password = forms.CharField(max_length=32,required=True, label=_("Parol"), min_length=8,widget=forms.PasswordInput())
    first_name = forms.CharField(max_length=10, required=True, label=_("Ism"))
    last_name = forms.CharField(max_length=10, required=True, label=_("Famliya"))

    def clean_first_name(self):
        data = str(self.cleaned_data.get('first_name'))
        if not re.match("^[A-Za-z]+$", data):
            raise ValidationError(_("Iltimos faqat lotin harflarinin kiriting!"))

        return data

    def clean_last_name(self):
        data = str(self.cleaned_data.get('last_name'))
        if not re.match("^[A-Za-z]+$", data):
            raise ValidationError(_("Iltimos faqat lotin harflarinin kiriting!"))

        return data

    def clean(self):
        data = super().clean()

        if data.get('password') != data.get('confirm'):
            raise ValidationError(
                {
                    "confirm": _("Parollar bir-xil emas")
                }
            )
        return data

    class Meta:
        model = User
        labels = {
            'username': 'Login'
        }
        fields = ('username', 'first_name', 'last_name', 'password',"confirm")

class ProfileForm(forms.ModelForm):
        first_name = forms.CharField(max_length=10, required=True, label=_("Ism"))
        last_name = forms.CharField(max_length=10, required=True, label=_("Famliya"))

        def clean_first_name(self):
            data = str(self.cleaned_data.get('first_name'))
            if not re.match("^[A-Za-z]+$", data):
                raise ValidationError(_("Iltimos faqat lotin harflarinin kiriting!"))

            return data

        def clean_last_name(self):
            data = str(self.cleaned_data.get('last_name'))
            if not re.match("^[A-Za-z]+$", data):
                raise ValidationError(_("Iltimos faqat lotin harflarinin kiriting!"))

            return data

        class Meta:
            model = User
            labels = {
                'username': 'Login'
            }
            fields = ('username', 'first_name', 'last_name')

class ChangePasswordForm(forms.Form):
    password = forms.CharField(max_length=32,required=True,label=_("Parol") ,min_length=8,widget=forms.PasswordInput())
    new_password = forms.CharField(max_length=32,required=True,label=_("Yangi parol") ,min_length=8,widget=forms.PasswordInput())
    confirm = forms.CharField(max_length=32,required=True,label=_("Parol takroran") ,min_length=8,widget=forms.PasswordInput())

    def __init__(self ,user,*args,**kwarsgs):
        super().__init__(*args,**kwarsgs)
        self.user = user # type: User


    def clean_password(self):

        if not check_password(self.cleaned_data.get('password'),self.user.password):
            raise ValidationError( _("Parol noto'g'ri"))
        return self.cleaned_data['password']

    def clean(self):
        data = super().clean()

        if data.get('new_password') != data.get('confirm'):
            raise ValidationError(
                {
                    "confirm": _("Parollar bir-xil emas")
                }
            )
        return