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
    ip, is_routable = get_client_ip()
    if ip is None:
        ip = "0.0.0.0"

    class Meta:
        model = user_model
        fields = "__all__"

    def clean(self):
        image = self.cleaned_data.get('image')
        if image > 2345678:
            self._errors["image"] = ErrorList([u"Image too heavy."])