from django.contrib import admin
from .models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'sex', 'birth_date')
    list_filter = ('name', 'surname', 'sex')
    search_fields = ('name', 'surname', 'birth_date')
    ordering = ('id',)
    list_per_page = 100
