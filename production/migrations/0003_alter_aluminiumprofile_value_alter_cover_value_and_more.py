# Generated by Django 4.1.5 on 2023-02-07 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0002_rename_drivers_driver_driver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluminiumprofile',
            name='value',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='cover',
            name='value',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='driver',
            name='value',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='lightmodule',
            name='value',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='mountingsystem',
            name='value',
            field=models.IntegerField(default=0),
        ),
    ]