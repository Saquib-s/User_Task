# Generated by Django 3.1.2 on 2021-11-25 15:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0005_auto_20211125_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_model',
            name='full_name',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(regex='^[A-Z][-a-zA-Z]+$')]),
        ),
    ]
