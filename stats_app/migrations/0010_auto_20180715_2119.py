# Generated by Django 2.0.5 on 2018-07-16 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats_app', '0009_auto_20180715_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gunshot',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='gunshot',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]