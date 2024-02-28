
from rest_framework.decorators import api_view
from rest_framework.response import Response


from rest_framework import status
from .models import PassengerInfomation, DriverInformation, RideInformation
from .serializers import PassengerInformationSerializer, DriverInformationSerializer, RideInormationSerializer

driver_email = ""

@api_view(["GET"])
def api_endpoints(request):
    context = [
        "localahost://8000/passenger-signup",
        "localahost://8000/passenger-login",
        "localahost://8000/driver-signup",
        "localahost://8000/driver-login",
        "localahost://8000/create-ride",
    ]
    return Response(context, status=status.HTTP_200_OK)

@api_view(["POST"])
def passenger_signup(request):
    serializer = PassengerInformationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response("User information is invalid", status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def passenger_login(request):

    key = request.data["email_address"]
    
    try:
        user = PassengerInfomation.objects.get(email_address=key)
    except PassengerInfomation.DoesNotExist:
        return Response("User not found", status=status.HTTP_404_NOT_FOUND)
    
    serializer = PassengerInformationSerializer(user, many=False)
    return Response(serializer.data, status=status.HTTP_302_FOUND)



@api_view(["POST"])
def driver_signup(request):
    serializer = DriverInformationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response("Driver information is invalid", status=status.HTTP_226_IM_USED)

@api_view(["POST"])
def driver_login(request):
    key = request.data["email_address"]
    try:
        user = DriverInformation.objects.get(email_address=key)
    except DriverInformation.DoesNotExist:
        return Response("User not found", status=status.HTTP_404_NOT_FOUND)
    
    request.session["key"] = key
    serializer = DriverInformationSerializer(user, many=False)
    return Response(serializer.data, status=status.HTTP_302_FOUND)

@api_view(["POST"])
def create_ride(request):
    user = DriverInformation.objects.get(email_address = request.session.get("key"))
    serializer = DriverInformationSerializer(user, many=False)
    requred_driver_info = {}
    for key, value in serializer.data.items():
        if key == "id" or key == "gender" or key == "phone" or key == "email_address" or key == "licence_id":
            continue
        requred_driver_info[key] = value
    
    driver_email = {"driver_email": request.session.get("key")}
    serializer_data_with_email = {**request.data, **driver_email}

    serializer = RideInormationSerializer(data=serializer_data_with_email)
    if serializer.is_valid():
        serializer.save()
        ride_info = {**requred_driver_info, **serializer.data}
        return Response(ride_info, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

