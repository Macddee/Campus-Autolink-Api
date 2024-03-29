# Generated by Django 5.0.2 on 2024-02-25 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DriverInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('email_address', models.EmailField(max_length=254)),
                ('licence_id', models.CharField(max_length=25)),
                ('vehicle_model', models.CharField(max_length=50)),
                ('vehicle_reg', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='PassengerInfomation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('email_address', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='RideInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_email', models.EmailField(max_length=254)),
                ('pick_point', models.CharField(max_length=250)),
                ('drop_point', models.CharField(max_length=250)),
                ('available_seats', models.IntegerField()),
                ('depature_time', models.DateTimeField()),
            ],
        ),
    ]
