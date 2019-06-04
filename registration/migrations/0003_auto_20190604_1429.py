# Generated by Django 2.2.1 on 2019-06-04 08:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registration', '0002_auto_20190528_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='batch',
            field=models.CharField(default='SRIP19-BATCH1', max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='effort',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='function_points',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='mentor',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='report',
            field=models.URLField(default='https://github.com/aditya3498/SRIP2019-Batch1/wiki'),
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
