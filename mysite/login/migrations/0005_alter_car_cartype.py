# Generated by Django 4.0.1 on 2022-01-25 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_ride_cartype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='cartype',
            field=models.CharField(max_length=128),
        ),
    ]