from django.db import models
from django.contrib.gis.db.models import PointField
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.deletion import SET_NULL


# Create your models here.


class Passenger(models.Model):
    name = models.CharField(max_length=256)
    identification_number = models.CharField(max_length=50, null=True)
    registered_user = models.ForeignKey("core.User", null=True, on_delete=SET_NULL)

    created_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Schedule(models.Model):
    name = models.CharField(max_length=256)

    estimated_departure_time = models.DateTimeField()
    estimated_arrival_time = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Bus(models.Model):
    name = models.CharField(max_length=256)
    patent = models.CharField(max_length=16)

    created_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Seats(models.Model):
    number = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )

    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    is_avail = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {}".format(self.bus.name, self.number)

    def __unicode__(self):
        return "{} {}".format(self.bus.name, self.number)


class Station(models.Model):
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    geo_location = PointField()

    created_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class TravelRoute(models.Model):
    name = models.CharField(max_length=256)
    origin = models.ForeignKey(
        Station, on_delete=models.SET_NULL, related_name="fk_travel_origin", null=True
    )
    destination = models.ForeignKey(
        Station,
        on_delete=models.SET_NULL,
        related_name="fk_travel_destination",
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Travel(models.Model):
    name = models.CharField(max_length=256)
    route = models.ForeignKey(TravelRoute, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    driver = models.ForeignKey("core.User", on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)

    price = models.IntegerField(validators=[MinValueValidator(0)])

    created_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class User(AbstractUser):
    class Profile(models.TextChoices):
        TICKET_VENDOR = u"TICKET_VENDOR", "Ticket Vendor"
        PASSENGER = u"PASSENGER", "Passenger"
        DRIVER = u"DRIVER", "Driver"

    class IdentificationType(models.TextChoices):
        PASSPORT = u"PASSPORT", "Passport"
        NATIONAL_ID_NUMBER = u"NATIONAL_ID_NUMBER", "National id number"  # eg: rut

    name = models.CharField(max_length=256)
    profile = models.CharField(
        max_length=16, choices=Profile.choices, default=Profile.PASSENGER
    )
    identification_type = models.CharField(
        max_length=18,
        choices=IdentificationType.choices,
        default=IdentificationType.NATIONAL_ID_NUMBER,
    )
    identification_number = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
