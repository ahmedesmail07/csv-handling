from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Restaurants

@admin.register(Restaurants)
class RestaurantsAdmin(ImportExportModelAdmin):
    pass

#Handling the CSV data with django-import-export