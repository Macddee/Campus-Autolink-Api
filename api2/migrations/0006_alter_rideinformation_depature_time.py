# Generated by Django 5.0.2 on 2024-02-26 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api2', '0005_alter_rideinformation_depature_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rideinformation',
            name='depature_time',
            field=models.TimeField(),
        ),
    ]