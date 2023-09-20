from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
    

    # def __init__(self, *args: Any, **kwargs: Any) -> None:
    #     super(SignUpForm,self).__init__(*args, **kwargs)

    #     for fieldName in ['username','email','password1','password2']:
    #         self.fields[fieldName].help_text = None

    