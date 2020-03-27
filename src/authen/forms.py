from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignUpForm(forms.Form):

    email = forms.EmailField()
    name = forms.CharField()
    password = forms.CharField()

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(SignUpForm, self).__init__(*args, **kwargs)