from django.urls import path
from . import views

urlpatterns = [
    path('passenger-signup', views.passenger_signup, name='passenger-signup'),
    path('passenger-login', views.passenger_login, name='passenger-login'),
    path("driver-signup", views.driver_signup, name="driver-signup"),
    path("driver-login", views.driver_login, name="driver-login"),
    path("create-ride", views.create_ride, name="create-ride"),

]