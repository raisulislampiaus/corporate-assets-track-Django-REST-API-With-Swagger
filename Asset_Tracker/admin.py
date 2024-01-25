from django.contrib import admin
from .models import Company, Device, Employee, DeviceAssignment

admin.site.site_header = "Asset Tracker API"
admin.site.site_title = "Corporate Asset Tracker Django REST API"
admin.site.index_title = "Welcome Admin"


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'phone_number')
    search_fields = ('name',)


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'serial_number', 'condition', 'company', 'checked_out')
    search_fields = ('name', 'serial_number')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    search_fields = ('company', 'devices')


@admin.register(DeviceAssignment)
class DeviceAssignmentAdmin(admin.ModelAdmin):
    list_display = ('device', 'employee', 'assigned_date', 'return_date', 'updated_at')
    search_fields = ('device', 'employee__name')
