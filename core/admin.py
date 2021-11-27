from django.contrib import admin
from . import models


class PassengerAdmin(admin.ModelAdmin):

    list_display = ("id", "name", "created_at", "modify_at")
    list_filter = (
        "created_at",
        "modify_at",
        "id",
        "name",
        "created_at",
        "modify_at",
    )
    search_fields = ("name",)
    date_hierarchy = "created_at"


class ScheduleAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "estimated_departure_time",
        "estimated_arrival_time",
        "created_at",
        "modify_at",
    )
    list_filter = (
        "estimated_departure_time",
        "estimated_arrival_time",
        "created_at",
        "modify_at",
        "id",
        "name",
        "estimated_departure_time",
        "estimated_arrival_time",
        "created_at",
        "modify_at",
    )
    search_fields = ("name",)
    date_hierarchy = "created_at"


class BusAdmin(admin.ModelAdmin):

    list_display = ("id", "name", "patent", "created_at", "modify_at")
    list_filter = (
        "created_at",
        "modify_at",
        "id",
        "name",
        "patent",
        "created_at",
        "modify_at",
    )
    search_fields = ("name",)
    date_hierarchy = "created_at"


class SeatsAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "number",
        "bus",
        "is_avail",
        "created_at",
        "modify_at",
    )
    list_filter = (
        "bus",
        "is_avail",
        "created_at",
        "modify_at",
        "id",
        "number",
        "bus",
        "is_avail",
        "created_at",
        "modify_at",
    )
    date_hierarchy = "created_at"


class UserAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "password",
        "last_login",
        "is_superuser",
        "username",
        "first_name",
        "last_name",
        "email",
        "is_staff",
        "is_active",
        "date_joined",
        "name",
        "profile",
        "identification_type",
        "identification_number",
        "created_at",
        "modify_at",
    )
    list_filter = (
        "last_login",
        "is_superuser",
        "is_staff",
        "is_active",
        "date_joined",
        "created_at",
        "modify_at",
        "id",
        "password",
        "last_login",
        "is_superuser",
        "username",
        "first_name",
        "last_name",
        "email",
        "is_staff",
        "is_active",
        "date_joined",
        "name",
        "profile",
        "identification_type",
        "identification_number",
        "created_at",
        "modify_at",
    )
    raw_id_fields = ("groups", "user_permissions")
    search_fields = ("name",)
    date_hierarchy = "created_at"


class StationAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "address",
        "geo_location",
        "created_at",
        "modify_at",
    )
    list_filter = (
        "created_at",
        "modify_at",
        "id",
        "name",
        "address",
        "geo_location",
        "created_at",
        "modify_at",
    )
    search_fields = ("name",)
    date_hierarchy = "created_at"


class TravelRouteAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "origin",
        "destination",
        "created_at",
        "modify_at",
    )
    list_filter = (
        "origin",
        "destination",
        "created_at",
        "modify_at",
        "id",
        "name",
        "origin",
        "destination",
        "created_at",
        "modify_at",
    )
    search_fields = ("name",)
    date_hierarchy = "created_at"


class TravelAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "route",
        "bus",
        "driver",
        "schedule",
        "price",
        "created_at",
        "modify_at",
    )
    list_filter = (
        "route",
        "bus",
        "driver",
        "schedule",
        "created_at",
        "modify_at",
        "id",
        "name",
        "route",
        "bus",
        "driver",
        "schedule",
        "price",
        "created_at",
        "modify_at",
    )
    search_fields = ("name",)
    date_hierarchy = "created_at"


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Passenger, PassengerAdmin)
_register(models.Schedule, ScheduleAdmin)
_register(models.Bus, BusAdmin)
_register(models.Seats, SeatsAdmin)
_register(models.User, UserAdmin)
_register(models.Station, StationAdmin)
_register(models.TravelRoute, TravelRouteAdmin)
_register(models.Travel, TravelAdmin)
