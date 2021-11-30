from rest_framework.serializers import ModelSerializer
from core.models import (
    Passenger,
    Schedule,
    Bus,
    Seats,
    Station,
    TravelRoute,
    Travel,
    User,
)


class PassengerSerializer(ModelSerializer):
    class Meta:
        model = Passenger
        depth = 2
        fields = "__all__"


class ScheduleSerializer(ModelSerializer):
    class Meta:
        model = Schedule
        depth = 2
        fields = "__all__"


class BusSerializer(ModelSerializer):
    class Meta:
        model = Bus
        depth = 2
        fields = "__all__"


class SeatsSerializer(ModelSerializer):
    class Meta:
        model = Seats
        depth = 2
        fields = "__all__"


class StationSerializer(ModelSerializer):
    class Meta:
        model = Station
        depth = 2
        fields = "__all__"


class TravelRouteSerializer(ModelSerializer):
    class Meta:
        model = TravelRoute
        depth = 2
        fields = "__all__"


class TravelSerializer(ModelSerializer):
    class Meta:
        model = Travel
        depth = 2
        fields = "__all__"



USER_FIELDS = (
        'id', 
        'username', 
        'first_name', 
        'last_name', 
        'email', 
        'date_joined', 
        'name', 
        'profile', 
        'identification_type', 
        'identification_number', 
        'created_at', 
        'modify_at', 
    )

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        depth = 2
        fields = USER_FIELDS

class DriverSerializer(ModelSerializer):
    class Meta:
        model = User
        depth = 2
        fields = USER_FIELDS
