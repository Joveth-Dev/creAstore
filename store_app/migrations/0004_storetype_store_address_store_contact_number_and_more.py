# Generated by Django 5.0.1 on 2024-01-10 04:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0003_store_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Store Type')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='store',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Store Address'),
        ),
        migrations.AddField(
            model_name='store',
            name='contact_number',
            field=models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.RegexValidator(message='Enter a valid Philippine phone number.', regex='^\\+?63(?:\\d{9}|\\d{10})$')]),
        ),
        migrations.AddField(
            model_name='store',
            name='description',
            field=models.TextField(default='+'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='store',
            name='open_from',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='store',
            name='open_to',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]