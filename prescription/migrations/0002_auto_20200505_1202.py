# Generated by Django 3.0.6 on 2020-05-05 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prescription', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescriptions',
            name='os_cyl',
            field=models.CharField(blank=True, max_length=56, null=True),
        ),
        migrations.AddField(
            model_name='prescriptions',
            name='os_dia',
            field=models.CharField(blank=True, max_length=56, null=True),
        ),
    ]
