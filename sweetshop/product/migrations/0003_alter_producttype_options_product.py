# Generated by Django 4.1.3 on 2022-11-23 18:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_create_producttype'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producttype',
            options={'ordering': ('name',)},
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, validators=[django.core.validators.MinLengthValidator(5)])),
                ('description', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(10)])),
                ('image', models.ImageField(blank=True, upload_to='cakes/')),
                ('price', models.FloatField()),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.producttype')),
            ],
        ),
    ]
