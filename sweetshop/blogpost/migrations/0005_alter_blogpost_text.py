# Generated by Django 4.1.3 on 2022-12-04 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0004_alter_blogpost_options_alter_blogpost_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='text',
            field=models.TextField(max_length=1000),
        ),
    ]
