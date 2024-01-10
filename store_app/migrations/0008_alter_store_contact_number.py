# Generated by Django 5.0.1 on 2024-01-10 05:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0007_alter_store_contact_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='contact_number',
            field=models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.RegexValidator(message='Enter a valid phone number.', regex='^\\+?(?:63)?(?:\\d{10}|\\d{11})$')]),
        ),
    ]