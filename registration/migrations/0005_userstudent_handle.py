# Generated by Django 2.2.1 on 2019-06-04 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_auto_20190604_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstudent',
            name='handle',
            field=models.CharField(default='handle', max_length=120),
            preserve_default=False,
        ),
    ]
