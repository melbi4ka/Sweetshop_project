# Generated by Django 4.1.3 on 2022-11-29 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0002_make_blogpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='blogpost',
            name='tagged_posts',
            field=models.ManyToManyField(blank=True, to='blogpost.tag'),
        ),
    ]
