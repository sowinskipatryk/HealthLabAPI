from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient')
    search_fields = ('id',)
    ordering = ('id',)
    list_per_page = 100
