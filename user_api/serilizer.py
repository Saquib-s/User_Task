from phonenumber_field.widgets import PhoneNumberPrefixWidget
from phonenumber_field.formfields import PhoneNumberField
from ipware import get_client_ip
from django.forms.utils import ErrorList

from rest_framework import serializers
from .models import user_model


class User_Serializer(serializers.ModelSerializer):
    phone_number = PhoneNumberField(
        widget=PhoneNumberPrefixWidget(initial='IN')
    )
    class Meta:
        model = user_model
        fields = '__all__'