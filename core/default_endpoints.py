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

# ModelViewSet
class PassengerModelViewSet(ModelViewSet):
    queryset = Passenger.objects.order_by("pk")
    serializer_class = PassengerSerializer


class ScheduleModelViewSet(ModelViewSet):
    queryset = Schedule.objects.order_by("pk")
    serializer_class = ScheduleSerializer


class BusModelViewSet(ModelViewSet):
    queryset = Bus.objects.order_by("pk")
    serializer_class = BusSerializer


class SeatsModelViewSet(ModelViewSet):
    queryset = Seats.objects.order_by("pk")
    serializer_class = SeatsSerializer


class StationModelViewSet(ModelViewSet):
    queryset = Station.objects.order_by("pk")
    serializer_class = StationSerializer


class TravelRouteModelViewSet(ModelViewSet):
    queryset = TravelRoute.objects.order_by("pk")
    serializer_class = TravelRouteSerializer


class TravelModelViewSet(ModelViewSet):
    queryset = Travel.objects.order_by("pk")
    serializer_class = TravelSerializer


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.order_by("pk")
    serializer_class = UserSerializer


# ViewSet
class PassengerViewSet(ViewSet):
    def list(self, request):
        queryset = Passenger.objects.order_by("pk")
        serializer = PassengerSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = PassengerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Passenger.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = PassengerSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Passenger.objects.get(pk=pk)
        except Passenger.DoesNotExist:
            return Response(status=404)
        serializer = PassengerSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Passenger.objects.get(pk=pk)
        except Passenger.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class ScheduleViewSet(ViewSet):
    def list(self, request):
        queryset = Schedule.objects.order_by("pk")
        serializer = ScheduleSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Schedule.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = ScheduleSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Schedule.objects.get(pk=pk)
        except Schedule.DoesNotExist:
            return Response(status=404)
        serializer = ScheduleSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Schedule.objects.get(pk=pk)
        except Schedule.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class BusViewSet(ViewSet):
    def list(self, request):
        queryset = Bus.objects.order_by("pk")
        serializer = BusSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = BusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Bus.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = BusSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Bus.objects.get(pk=pk)
        except Bus.DoesNotExist:
            return Response(status=404)
        serializer = BusSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Bus.objects.get(pk=pk)
        except Bus.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class SeatsViewSet(ViewSet):
    def list(self, request):
        queryset = Seats.objects.order_by("pk")
        serializer = SeatsSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = SeatsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Seats.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = SeatsSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Seats.objects.get(pk=pk)
        except Seats.DoesNotExist:
            return Response(status=404)
        serializer = SeatsSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Seats.objects.get(pk=pk)
        except Seats.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class StationViewSet(ViewSet):
    def list(self, request):
        queryset = Station.objects.order_by("pk")
        serializer = StationSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = StationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Station.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = StationSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Station.objects.get(pk=pk)
        except Station.DoesNotExist:
            return Response(status=404)
        serializer = StationSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Station.objects.get(pk=pk)
        except Station.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class TravelRouteViewSet(ViewSet):
    def list(self, request):
        queryset = TravelRoute.objects.order_by("pk")
        serializer = TravelRouteSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = TravelRouteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = TravelRoute.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = TravelRouteSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = TravelRoute.objects.get(pk=pk)
        except TravelRoute.DoesNotExist:
            return Response(status=404)
        serializer = TravelRouteSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = TravelRoute.objects.get(pk=pk)
        except TravelRoute.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class TravelViewSet(ViewSet):
    def list(self, request):
        queryset = Travel.objects.order_by("pk")
        serializer = TravelSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = TravelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Travel.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = TravelSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Travel.objects.get(pk=pk)
        except Travel.DoesNotExist:
            return Response(status=404)
        serializer = TravelSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Travel.objects.get(pk=pk)
        except Travel.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class UserViewSet(ViewSet):
    def list(self, request):
        queryset = User.objects.order_by("pk")
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=404)
        serializer = UserSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


# APIView


class PassengerAPIView(APIView):
    def get(self, request, id, format=None):
        try:
            item = Passenger.objects.get(pk=id)
            serializer = PassengerSerializer(item)
            return Response(serializer.data)
        except Passenger.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Passenger.objects.get(pk=id)
        except Passenger.DoesNotExist:
            return Response(status=404)
        serializer = PassengerSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Passenger.objects.get(pk=id)
        except Passenger.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class PassengerAPIListView(APIView):
    def get(self, request, format=None):
        items = Passenger.objects.order_by("pk")
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = PassengerSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = PassengerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class ScheduleAPIView(APIView):
    def get(self, request, id, format=None):
        try:
            item = Schedule.objects.get(pk=id)
            serializer = ScheduleSerializer(item)
            return Response(serializer.data)
        except Schedule.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Schedule.objects.get(pk=id)
        except Schedule.DoesNotExist:
            return Response(status=404)
        serializer = ScheduleSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Schedule.objects.get(pk=id)
        except Schedule.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class ScheduleAPIListView(APIView):
    def get(self, request, format=None):
        items = Schedule.objects.order_by("pk")
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = ScheduleSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = ScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class BusAPIView(APIView):
    def get(self, request, id, format=None):
        try:
            item = Bus.objects.get(pk=id)
            serializer = BusSerializer(item)
            return Response(serializer.data)
        except Bus.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Bus.objects.get(pk=id)
        except Bus.DoesNotExist:
            return Response(status=404)
        serializer = BusSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Bus.objects.get(pk=id)
        except Bus.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class BusAPIListView(APIView):
    def get(self, request, format=None):
        items = Bus.objects.order_by("pk")
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = BusSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = BusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class SeatsAPIView(APIView):
    def get(self, request, id, format=None):
        try:
            item = Seats.objects.get(pk=id)
            serializer = SeatsSerializer(item)
            return Response(serializer.data)
        except Seats.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Seats.objects.get(pk=id)
        except Seats.DoesNotExist:
            return Response(status=404)
        serializer = SeatsSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Seats.objects.get(pk=id)
        except Seats.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class SeatsAPIListView(APIView):
    def get(self, request, format=None):
        items = Seats.objects.order_by("pk")
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = SeatsSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = SeatsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class StationAPIView(APIView):
    def get(self, request, id, format=None):
        try:
            item = Station.objects.get(pk=id)
            serializer = StationSerializer(item)
            return Response(serializer.data)
        except Station.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Station.objects.get(pk=id)
        except Station.DoesNotExist:
            return Response(status=404)
        serializer = StationSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Station.objects.get(pk=id)
        except Station.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class StationAPIListView(APIView):
    def get(self, request, format=None):
        items = Station.objects.order_by("pk")
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = StationSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = StationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class TravelRouteAPIView(APIView):
    def get(self, request, id, format=None):
        try:
            item = TravelRoute.objects.get(pk=id)
            serializer = TravelRouteSerializer(item)
            return Response(serializer.data)
        except TravelRoute.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = TravelRoute.objects.get(pk=id)
        except TravelRoute.DoesNotExist:
            return Response(status=404)
        serializer = TravelRouteSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = TravelRoute.objects.get(pk=id)
        except TravelRoute.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class TravelRouteAPIListView(APIView):
    def get(self, request, format=None):
        items = TravelRoute.objects.order_by("pk")
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = TravelRouteSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = TravelRouteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class TravelAPIView(APIView):
    def get(self, request, id, format=None):
        try:
            item = Travel.objects.get(pk=id)
            serializer = TravelSerializer(item)
            return Response(serializer.data)
        except Travel.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Travel.objects.get(pk=id)
        except Travel.DoesNotExist:
            return Response(status=404)
        serializer = TravelSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Travel.objects.get(pk=id)
        except Travel.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class TravelAPIListView(APIView):
    def get(self, request, format=None):
        items = Travel.objects.order_by("pk")
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = TravelSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = TravelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class UserAPIView(APIView):
    def get(self, request, id, format=None):
        try:
            item = User.objects.get(pk=id)
            serializer = UserSerializer(item)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = User.objects.get(pk=id)
        except User.DoesNotExist:
            return Response(status=404)
        serializer = UserSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = User.objects.get(pk=id)
        except User.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class UserAPIListView(APIView):
    def get(self, request, format=None):
        items = User.objects.order_by("pk")
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = UserSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


# function


@api_view(["GET", "POST"])
def passenger_list(request):
    if request.method == "GET":
        items = Passenger.objects.order_by("pk")
        serializer = PassengerSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = PassengerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(["GET", "PUT", "DELETE"])
def passenger_detail(request, pk):
    try:
        item = Passenger.objects.get(pk=pk)
    except Passenger.DoesNotExist:
        return Response(status=404)

    if request.method == "GET":
        serializer = PassengerSerializer(item)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = PassengerSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == "DELETE":
        item.delete()
        return Response(status=204)


@api_view(["GET", "POST"])
def schedule_list(request):
    if request.method == "GET":
        items = Schedule.objects.order_by("pk")
        serializer = ScheduleSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(["GET", "PUT", "DELETE"])
def schedule_detail(request, pk):
    try:
        item = Schedule.objects.get(pk=pk)
    except Schedule.DoesNotExist:
        return Response(status=404)

    if request.method == "GET":
        serializer = ScheduleSerializer(item)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ScheduleSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == "DELETE":
        item.delete()
        return Response(status=204)


@api_view(["GET", "POST"])
def bus_list(request):
    if request.method == "GET":
        items = Bus.objects.order_by("pk")
        serializer = BusSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = BusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(["GET", "PUT", "DELETE"])
def bus_detail(request, pk):
    try:
        item = Bus.objects.get(pk=pk)
    except Bus.DoesNotExist:
        return Response(status=404)

    if request.method == "GET":
        serializer = BusSerializer(item)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = BusSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == "DELETE":
        item.delete()
        return Response(status=204)


@api_view(["GET", "POST"])
def seats_list(request):
    if request.method == "GET":
        items = Seats.objects.order_by("pk")
        serializer = SeatsSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = SeatsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(["GET", "PUT", "DELETE"])
def seats_detail(request, pk):
    try:
        item = Seats.objects.get(pk=pk)
    except Seats.DoesNotExist:
        return Response(status=404)

    if request.method == "GET":
        serializer = SeatsSerializer(item)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = SeatsSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == "DELETE":
        item.delete()
        return Response(status=204)


@api_view(["GET", "POST"])
def station_list(request):
    if request.method == "GET":
        items = Station.objects.order_by("pk")
        serializer = StationSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = StationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(["GET", "PUT", "DELETE"])
def station_detail(request, pk):
    try:
        item = Station.objects.get(pk=pk)
    except Station.DoesNotExist:
        return Response(status=404)

    if request.method == "GET":
        serializer = StationSerializer(item)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = StationSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == "DELETE":
        item.delete()
        return Response(status=204)


@api_view(["GET", "POST"])
def travelroute_list(request):
    if request.method == "GET":
        items = TravelRoute.objects.order_by("pk")
        serializer = TravelRouteSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = TravelRouteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(["GET", "PUT", "DELETE"])
def travelroute_detail(request, pk):
    try:
        item = TravelRoute.objects.get(pk=pk)
    except TravelRoute.DoesNotExist:
        return Response(status=404)

    if request.method == "GET":
        serializer = TravelRouteSerializer(item)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = TravelRouteSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == "DELETE":
        item.delete()
        return Response(status=204)


@api_view(["GET", "POST"])
def travel_list(request):
    if request.method == "GET":
        items = Travel.objects.order_by("pk")
        serializer = TravelSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = TravelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(["GET", "PUT", "DELETE"])
def travel_detail(request, pk):
    try:
        item = Travel.objects.get(pk=pk)
    except Travel.DoesNotExist:
        return Response(status=404)

    if request.method == "GET":
        serializer = TravelSerializer(item)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = TravelSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == "DELETE":
        item.delete()
        return Response(status=204)


@api_view(["GET", "POST"])
def user_list(request):
    if request.method == "GET":
        items = User.objects.order_by("pk")
        serializer = UserSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(["GET", "PUT", "DELETE"])
def user_detail(request, pk):
    try:
        item = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=404)

    if request.method == "GET":
        serializer = UserSerializer(item)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = UserSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == "DELETE":
        item.delete()
        return Response(status=204)
