from rest_framework.decorators import api_view
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import SimpleRouter
from django.conf.urls import include, url
from django.urls import path
from rest_framework_swagger.views import get_swagger_view
from core import default_endpoints, endpoints, views


viewset_router = SimpleRouter()
# ModelViewSet(mvs)
viewset_router.register(r"api/modelviewset/passenger", default_endpoints.PassengerModelViewSet)
viewset_router.register(r"api/modelviewset/schedule", default_endpoints.ScheduleModelViewSet)
viewset_router.register(r"api/modelviewset/bus", default_endpoints.BusModelViewSet)
viewset_router.register(r"api/modelviewset/seats", default_endpoints.SeatsModelViewSet)
viewset_router.register(r"api/modelviewset/station", default_endpoints.StationModelViewSet)
viewset_router.register(r"api/modelviewset/travelroute", default_endpoints.TravelRouteModelViewSet)
viewset_router.register(r"api/modelviewset/travel", default_endpoints.TravelModelViewSet)
viewset_router.register(r"api/modelviewset/user", default_endpoints.UserModelViewSet)
# ViewSet(vs)
viewset_router.register(r"api/viewset/passenger", default_endpoints.PassengerViewSet, "Passenger")
viewset_router.register(r"api/viewset/schedule", default_endpoints.ScheduleViewSet, "Schedule")
viewset_router.register(r"api/viewset/bus", default_endpoints.BusViewSet, "Bus")
viewset_router.register(r"api/viewset/seats", default_endpoints.SeatsViewSet, "Seats")
viewset_router.register(r"api/viewset/station", default_endpoints.StationViewSet, "Station")
viewset_router.register(r"api/viewset/travelroute", default_endpoints.TravelRouteViewSet, "TravelRoute")
viewset_router.register(r"api/viewset/travel", default_endpoints.TravelViewSet, "Travel")
viewset_router.register(r"api/viewset/user", default_endpoints.UserViewSet, "User")

api_views = [
    url(r"^api/views/passenger/(?P<id>[0-9]+)/$", default_endpoints.PassengerAPIView.as_view()),
    url(r"^api/views/passenger/$", default_endpoints.PassengerAPIListView.as_view()),
    url(r"^api/views/schedule/(?P<id>[0-9]+)/$", default_endpoints.ScheduleAPIView.as_view()),
    url(r"^api/views/schedule/$", default_endpoints.ScheduleAPIListView.as_view()),
    url(r"^api/views/bus/(?P<id>[0-9]+)/$", default_endpoints.BusAPIView.as_view()),
    url(r"^api/views/bus/$", default_endpoints.BusAPIListView.as_view()),
    url(r"^api/views/seats/(?P<id>[0-9]+)/$", default_endpoints.SeatsAPIView.as_view()),
    url(r"^api/views/seats/$", default_endpoints.SeatsAPIListView.as_view()),
    url(r"^api/views/station/(?P<id>[0-9]+)/$", default_endpoints.StationAPIView.as_view()),
    url(r"^api/views/station/$", default_endpoints.StationAPIListView.as_view()),
    url(r"^api/views/travelroute/(?P<id>[0-9]+)/$", default_endpoints.TravelRouteAPIView.as_view()),
    url(r"^api/views/travelroute/$", default_endpoints.TravelRouteAPIListView.as_view()),
    url(r"^api/views/travel/(?P<id>[0-9]+)/$", default_endpoints.TravelAPIView.as_view()),
    url(r"^api/views/travel/$", default_endpoints.TravelAPIListView.as_view()),
    url(r"^api/views/user/(?P<id>[0-9]+)/$", default_endpoints.UserAPIView.as_view()),
    url(r"^api/views/user/$", default_endpoints.UserAPIListView.as_view()),
]

function_views = format_suffix_patterns(
    [
        url(r"^api/function_views/passenger/(?P<pk>[0-9]+)/$", default_endpoints.passenger_detail),
        url(r"^api/function_views/passenger/$", default_endpoints.passenger_list),
        url(r"^api/function_views/schedule/(?P<pk>[0-9]+)/$", default_endpoints.schedule_detail),
        url(r"^api/function_views/schedule/$", default_endpoints.schedule_list),
        url(r"^api/function_views/bus/(?P<pk>[0-9]+)/$", default_endpoints.bus_detail),
        url(r"^api/function_views/bus/$", default_endpoints.bus_list),
        url(r"^api/function_views/seats/(?P<pk>[0-9]+)/$", default_endpoints.seats_detail),
        url(r"^api/function_views/seats/$", default_endpoints.seats_list),
        url(r"^api/function_views/station/(?P<pk>[0-9]+)/$", default_endpoints.station_detail),
        url(r"^api/function_views/station/$", default_endpoints.station_list),
        url(r"^api/function_views/travelroute/(?P<pk>[0-9]+)/$", default_endpoints.travelroute_detail),
        url(r"^api/function_views/travelroute/$", default_endpoints.travelroute_list),
        url(r"^api/function_views/travel/(?P<pk>[0-9]+)/$", default_endpoints.travel_detail),
        url(r"^api/function_views/travel/$", default_endpoints.travel_list),
        url(r"^api/function_views/user/(?P<pk>[0-9]+)/$", default_endpoints.user_detail),
        url(r"^api/function_views/user/$", default_endpoints.user_list),

        url(r"^api/function_views/driver/(?P<pk>[0-9]+)/$", endpoints.driver_detail),
        url(r"^api/function_views/driver/$", endpoints.driver_list),
    ]
)


api_doc = [
        url(r'^api/doc', get_swagger_view(title='Rest API Document'))
    ]


core_views = [
    path('', views.index, name='index'),
]


urlpatterns = core_views + viewset_router.urls + api_views + function_views + api_doc
