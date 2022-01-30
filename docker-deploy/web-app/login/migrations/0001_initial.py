# Generated by Django 4.0.1 on 2022-01-24 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupnumber', models.DecimalField(decimal_places=0, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('sex', models.CharField(choices=[('male', 'M'), ('female', 'F')], default='M', max_length=32)),
                ('driver', models.BooleanField(default=False)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'user',
                'ordering': ['-c_time'],
            },
        ),
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ownernumber', models.DecimalField(decimal_places=0, max_digits=3)),
                ('ridedriver', models.CharField(max_length=128, unique=True)),
                ('dest', models.CharField(max_length=256)),
                ('arrivaltime', models.DateTimeField(auto_now=True)),
                ('endtime', models.DateTimeField(auto_now=True)),
                ('share', models.BooleanField(default=False)),
                ('freeText', models.CharField(max_length=256)),
                ('status', models.DecimalField(decimal_places=0, max_digits=2)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='login.user')),
                ('sharer', models.ManyToManyField(through='login.Relationship', to='login.User')),
            ],
        ),
        migrations.AddField(
            model_name='relationship',
            name='ride',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.ride'),
        ),
        migrations.AddField(
            model_name='relationship',
            name='uesr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.user'),
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cartype', models.CharField(max_length=128, unique=True)),
                ('plateNumber', models.CharField(max_length=256)),
                ('passengersNumber', models.DecimalField(decimal_places=0, max_digits=3)),
                ('freeText', models.CharField(max_length=256)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='login.user')),
            ],
        ),
    ]