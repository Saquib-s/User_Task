from .models import user_model
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from phonenumber_field.formfields import PhoneNumberField
from django import forms
from ipware import get_client_ip
from django.forms.utils import ErrorList



class UserForm(forms.ModelForm):
    phone_number = PhoneNumberField(
        widget=PhoneNumberPrefixWidget(initial='IN')
    )

    class Meta:
        model = user_model
        fields = "__all__"

