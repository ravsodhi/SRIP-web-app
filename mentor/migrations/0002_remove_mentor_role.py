# Generated by Django 2.2.2 on 2019-06-28 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentor',
            name='role',
        ),
    ]
