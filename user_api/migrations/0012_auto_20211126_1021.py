# Generated by Django 3.1.2 on 2021-11-26 04:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0011_auto_20211126_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_model',
            name='full_name',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(regex='^(([A-Za-z]+[,.]?+[\\s]+?|[a-z]+?)+)$')]),
        ),
    ]
