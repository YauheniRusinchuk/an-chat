# Generated by Django 2.2 on 2019-04-21 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='slug',
            field=models.SlugField(default='dadada'),
            preserve_default=False,
        ),
    ]
