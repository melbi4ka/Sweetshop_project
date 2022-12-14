# Generated by Django 4.1.3 on 2022-11-17 17:01

import django.core.validators
from django.db import migrations, models
import sweetshop.webusers.validators


class Migration(migrations.Migration):

    dependencies = [
        ('webusers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='city',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='appuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='appuser',
            name='street',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='appuser',
            name='street_number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.MinLengthValidator(2), sweetshop.webusers.validators.validate_only_letters]),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.MinLengthValidator(2), sweetshop.webusers.validators.validate_only_letters]),
        ),
    ]