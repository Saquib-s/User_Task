from django.db import models
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class user_model(models.Model):
    gender_choices = [
        ('male','male'),
        ('female','female')
    ]
    full_name_regex = RegexValidator(regex=r'^[a-zA-Z]+(\s[a-zA-Z]+)?$')
    full_name = models.CharField(validators=[full_name_regex], max_length=17, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    ip_address = models.TextField(default=' ')
    country = models.CharField(max_length=100)
    gender = models.CharField(choices=gender_choices,max_length=10)
    image = models.ImageField(upload_to='image',null=True)
    phone = PhoneNumberField(null=True)
