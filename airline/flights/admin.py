from django.contrib import admin
from .models import Flight, Airport, Passenger
# Register your models here.

class FlightAdmin(admin.ModelAdmin):
    list_display = ("origin", "destination", "duration", "id")

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)

# can be opened by url: /admin
# tells django you can use admin to manipulate flight and airport
admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)
