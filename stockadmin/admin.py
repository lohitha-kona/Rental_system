from django.contrib import admin

# Register your models here.
from .models import AddBook,AddBicycle,AddManager,AddBike


admin.site.register(AddBook)
admin.site.register(AddBicycle)
admin.site.register(AddManager)
admin.site.register(AddBike)