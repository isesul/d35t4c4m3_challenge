from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from core.serializers import (
    PassengerSerializer,
    ScheduleSerializer,
    BusSerializer,
    SeatsSerializer,
    StationSerializer,
    TravelRouteSerializer,
    TravelSerializer,
    UserSerializer,
)
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

