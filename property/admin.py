from django.contrib import admin

from .models import Flat, Complaint

class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'id', 'owner')
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town',)
    list_editable = ('new_building',)
    readonly_fields = ('created_at',)
    list_filter = ('new_building', 'rooms_number', 'floor', 'has_balcony')


class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('user', 'flat', 'text', )
    raw_id_fields = ('user', 'flat')



admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)