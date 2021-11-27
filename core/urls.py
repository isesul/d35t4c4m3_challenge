from rest_framework.decorators import api_view
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import SimpleRouter
from django.conf.urls import include, url
from core import default_endpoints as views
from rest_framework_swagger.views import get_swagger_view

viewset_router = SimpleRouter()
# ModelViewSet(mvs)
viewset_router.register(r"api/modelviewset/passenger", views.PassengerModelViewSet)
viewset_router.register(r"api/modelviewset/schedule", views.ScheduleModelViewSet)
viewset_router.register(r"api/modelviewset/bus", views.BusModelViewSet)
viewset_router.register(r"api/modelviewset/seats", views.SeatsModelViewSet)
viewset_router.register(r"api/modelviewset/station", views.StationModelViewSet)
viewset_router.register(r"api/modelviewset/travelroute", views.TravelRouteModelViewSet)
viewset_router.register(r"api/modelviewset/travel", views.TravelModelViewSet)
viewset_router.register(r"api/modelviewset/user", views.UserModelViewSet)
# ViewSet(vs)
viewset_router.register(r"api/viewset/passenger", views.PassengerViewSet, "Passenger")
viewset_router.register(r"api/viewset/schedule", views.ScheduleViewSet, "Schedule")
viewset_router.register(r"api/viewset/bus", views.BusViewSet, "Bus")
viewset_router.register(r"api/viewset/seats", views.SeatsViewSet, "Seats")
viewset_router.register(r"api/viewset/station", views.StationViewSet, "Station")
viewset_router.register(r"api/viewset/travelroute", views.TravelRouteViewSet, "TravelRoute")
viewset_router.register(r"api/viewset/travel", views.TravelViewSet, "Travel")
viewset_router.register(r"api/viewset/user", views.UserViewSet, "User")

api_views = [
    url(r"^api/views/passenger/(?P<id>[0-9]+)/$", views.PassengerAPIView.as_view()),
    url(r"^api/views/passenger/$", views.PassengerAPIListView.as_view()),
    url(r"^api/views/schedule/(?P<id>[0-9]+)/$", views.ScheduleAPIView.as_view()),
    url(r"^api/views/schedule/$", views.ScheduleAPIListView.as_view()),
    url(r"^api/views/bus/(?P<id>[0-9]+)/$", views.BusAPIView.as_view()),
    url(r"^api/views/bus/$", views.BusAPIListView.as_view()),
    url(r"^api/views/seats/(?P<id>[0-9]+)/$", views.SeatsAPIView.as_view()),
    url(r"^api/views/seats/$", views.SeatsAPIListView.as_view()),
    url(r"^api/views/station/(?P<id>[0-9]+)/$", views.StationAPIView.as_view()),
    url(r"^api/views/station/$", views.StationAPIListView.as_view()),
    url(r"^api/views/travelroute/(?P<id>[0-9]+)/$", views.TravelRouteAPIView.as_view()),
    url(r"^api/views/travelroute/$", views.TravelRouteAPIListView.as_view()),
    url(r"^api/views/travel/(?P<id>[0-9]+)/$", views.TravelAPIView.as_view()),
    url(r"^api/views/travel/$", views.TravelAPIListView.as_view()),
    url(r"^api/views/user/(?P<id>[0-9]+)/$", views.UserAPIView.as_view()),
    url(r"^api/views/user/$", views.UserAPIListView.as_view()),
]

function_views = format_suffix_patterns(
    [
        url(r"^api/function_views/passenger/(?P<pk>[0-9]+)/$", views.passenger_detail),
        url(r"^api/function_views/passenger/$", views.passenger_list),
        url(r"^api/function_views/schedule/(?P<pk>[0-9]+)/$", views.schedule_detail),
        url(r"^api/function_views/schedule/$", views.schedule_list),
        url(r"^api/function_views/bus/(?P<pk>[0-9]+)/$", views.bus_detail),
        url(r"^api/function_views/bus/$", views.bus_list),
        url(r"^api/function_views/seats/(?P<pk>[0-9]+)/$", views.seats_detail),
        url(r"^api/function_views/seats/$", views.seats_list),
        url(r"^api/function_views/station/(?P<pk>[0-9]+)/$", views.station_detail),
        url(r"^api/function_views/station/$", views.station_list),
        url(r"^api/function_views/travelroute/(?P<pk>[0-9]+)/$", views.travelroute_detail),
        url(r"^api/function_views/travelroute/$", views.travelroute_list),
        url(r"^api/function_views/travel/(?P<pk>[0-9]+)/$", views.travel_detail),
        url(r"^api/function_views/travel/$", views.travel_list),
        url(r"^api/function_views/user/(?P<pk>[0-9]+)/$", views.user_detail),
        url(r"^api/function_views/user/$", views.user_list),
    ]
)


api_doc = [
        url(r'^api/doc', get_swagger_view(title='Rest API Document'))
    ]

urlpatterns = viewset_router.urls + api_views + function_views + api_doc
