from django import forms
from django.contrib.auth.forms import UserCreationForm
from Authentication.models import User 

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget= forms.text)
#we will use the model in our user app to interact with our form
    class Meta:
        model = User
        fields =['username', 'email']


