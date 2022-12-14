# Generated by Django 4.1.3 on 2022-12-07 12:11

import django.core.validators
from django.db import migrations, models
import helpers.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalLinkInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(max_length=100, unique=True, validators=[helpers.validators.validate_alphabet_characters, django.core.validators.MinLengthValidator(4)])),
                ('section_description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='SubscribedUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30, unique=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
