# Generated by Django 4.1.3 on 2022-12-11 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_subsections_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subsections',
            name='subsection_description',
            field=models.TextField(max_length=500),
        ),
    ]