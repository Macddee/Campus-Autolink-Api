from rest_framework import serializers
from .models import PassengerInfomation, DriverInformation, RideInformation

class PassengerInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassengerInfomation
        fields = "__all__"

class DriverInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverInformation
        fields = "__all__"

class RideInormationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideInformation
        fields = "__all__"