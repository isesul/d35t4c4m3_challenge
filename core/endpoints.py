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
    DriverSerializer,
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

@api_view(["GET", "POST"])
def driver_list(request):
    if request.method == "GET":
        items = User.objects.filter(profile=User.Profile.DRIVER).order_by("pk")
        serializer = DriverSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = DriverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(["GET", "PUT", "DELETE"])
def driver_detail(request, pk):
    try:
        item = User.objects.filter(profile=User.Profile.DRIVER).get(pk=pk)
    except User.DoesNotExist:
        return Response(status=404)

    if request.method == "GET":
        serializer = DriverSerializer(item)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = DriverSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == "DELETE":
        item.delete()
        return Response(status=204)
