from django.contrib import admin

# Register your models here.
from .models import Registration,Orders,BicycleOrders

admin.site.register(Registration)
admin.site.register(Orders)
admin.site.register(BicycleOrders)