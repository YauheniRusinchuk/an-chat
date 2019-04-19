from django import forms
from src.models.room.models import Room
from django.contrib.auth.hashers import make_password, check_password

#
# hashed_pwd = make_password("plain_text")
# check_password("plain_text",hashed_pwd)


class FormRoom(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model   = Room
        fields  = [
            'name',
            'password',
        ]


    def clean_password(self):
        hashed_pswd = make_password(self.cleaned_data.get('password'))
        return hashed_pswd
