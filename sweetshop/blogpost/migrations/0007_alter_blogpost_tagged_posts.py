# Generated by Django 4.1.3 on 2022-12-11 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0006_alter_blogpost_tagged_posts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='tagged_posts',
            field=models.ManyToManyField(blank=True, to='blogpost.tag'),
        ),
    ]
