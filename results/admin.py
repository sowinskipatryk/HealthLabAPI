from django.contrib import admin
from .models import Result


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('order', 'name', 'value', 'reference')
    list_filter = ('name', )
    search_fields = ('name', 'value')
    ordering = ('order', 'name')
    list_per_page = 100
