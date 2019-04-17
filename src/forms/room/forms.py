from django import forms
from src.models.room.models import Room

class FormRoom(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput(
             attrs={'placeholder': 'password ...'}
    ))

    class Meta:
        model   = Room
        fields  = [
            'name',
            'password',
        ]



    # name     = forms.CharField()
    #
    #name.widget.attrs.update({"placeholder" : "name room ..."})
