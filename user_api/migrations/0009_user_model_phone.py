# Generated by Django 3.1.2 on 2021-11-25 15:42

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0008_auto_20211125_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_model',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None),
        ),
    ]
