# Generated by Django 5.0.2 on 2024-02-26 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api2', '0003_alter_driverinformation_email_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rideinformation',
            name='depature_time',
            field=models.TimeField(),
        ),
    ]