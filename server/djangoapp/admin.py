# from django.contrib import admin
# from .models import related models


# Register your models here.

# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here
from django.contrib import admin
from .models import CarMake, CarModel


# This Inline lets you edit CarModels directly in CarMake admin
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1  # How many empty forms to display


# This defines how CarModel appears in admin separately (optional)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ["name", "car_make", "type", "year"]
    list_filter = ["car_make", "type", "year"]
    search_fields = ["name", "car_make__name"]


# This defines how CarMake appears in admin, with CarModels inline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]


# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
