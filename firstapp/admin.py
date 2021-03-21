from django.contrib import admin
from . models import Date_store
# Register your models here.
from import_export.admin import ImportExportModelAdmin

@admin.register(Date_store)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ['id', 'rate', 'date']

