# Generated by Django 3.1.2 on 2021-11-26 04:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0009_user_model_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_model',
            old_name='image_upload',
            new_name='image',
        ),
        migrations.AlterField(
            model_name='user_model',
            name='full_name',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Z]+([\\s][a-zA-Z]+)*')]),
        ),
        migrations.AlterField(
            model_name='user_model',
            name='ip_address',
            field=models.TextField(default=' '),
        ),
    ]