from django.contrib import admin
from .models import Address
from import_export.admin import ImportExportModelAdmin


# Register your models here.


@admin.register(Address)
class AddressAdmin(ImportExportModelAdmin):
    list_display = (
        'Name', 'Job', 'Address1', 'Address2', 'Area', 'City', 'State', 'Country', 'Pincode', 'latitude', 'longitude')
