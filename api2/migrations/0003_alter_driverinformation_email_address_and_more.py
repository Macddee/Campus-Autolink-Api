# Generated by Django 5.0.2 on 2024-02-25 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api2', '0002_alter_passengerinfomation_email_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driverinformation',
            name='email_address',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='rideinformation',
            name='driver_email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]