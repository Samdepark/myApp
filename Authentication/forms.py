from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from Authentication.models import User 
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

# class UserRegisterForm(UserCreationForm):
#     username = forms.CharField(widget= forms.text)
# #we will use the model in our user app to interact with our form
#     class Meta:
#         model = User
#         fields =['username', 'email']




PAYMENT_CHOICE = {
    ('P', 'paypal'),
    ('D', 'Debit'),
    ('M', 'M-Pesa')
}

class CheckoutForm(forms.Form):
    street_address = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder":"1123 Hiltone"
    }))
    apartment_address = forms.CharField(required=False, widget=forms.TextInput(attrs={
        "placeholder":"Apartment or Suit"
    }))
    country = CountryField(blank_label='(select country)').formfield(
        Widget = CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100'
    }))
    zip = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'id':'zip'
    }))
    same_biling_address = forms.BooleanField(widget=forms.CheckboxInput())
    save_info = forms.BooleanField(required=False)
    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICE )
