from django.contrib import admin
from .models import Flight, Airport
# Register your models here.

# can be opened by /admin
# tells django you can use admin to manipulate flight and airport
admin.site.register(Airport)
admin.site.register(Flight)