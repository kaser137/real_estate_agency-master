from django.contrib import admin

from .models import Flat

class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'id', 'owner')
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town',)
    list_editable = ('new_building',)
    readonly_fields = ('created_at',)
    list_filter = ('new_building', 'rooms_number', 'floor', 'has_balcony')



admin.site.register(Flat, FlatAdmin)