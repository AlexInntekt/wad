from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(forms.Form):

    email = forms.EmailField()
    name = forms.CharField()
    password = forms.CharField()

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(SignUpForm, self).__init__(*args, **kwargs)

    def clean_name(self):
        name = self.cleaned_data['name']
        userAlreadyExists = User.objects.filter(username=name)

        if userAlreadyExists.count != 0:
            raise forms.ValidationError("This username is already taken!")

        return name