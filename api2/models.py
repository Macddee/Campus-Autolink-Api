from django.db import models
from datetime import time


class PassengerInfomation(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    phone = models.IntegerField()
    email_address = models.EmailField(max_length=254,
                                      unique=True,
                                      null=False
                                    )

class DriverInformation(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    phone = models.IntegerField()
    email_address = models.EmailField(max_length=254,
                                      unique=True,
                                      null=False
                                    )
    licence_id = models.CharField(max_length=25)
    vehicle_model = models.CharField(max_length=50)
    vehicle_reg = models.CharField(max_length=8)


class RideInformation(models.Model):
    
    pick_point = models.CharField(max_length=250)
    drop_point = models.CharField(max_length=250)
    available_seats = models.IntegerField()
    depature_time = models.TimeField()
    driver_email = models.EmailField(max_length=254,
                                      unique=True,
                                      null=False
                                    )
