# Generated by Django 2.1.4 on 2019-06-12 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0009_auto_20190612_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='area_interest',
            field=models.CharField(choices=[('MachineLearning', 'Machine Learning'), ('Programming', 'Programming'), ('WebDev', 'Web Development')], max_length=120),
        ),
    ]