from django.contrib import admin

from .models import Flat, Complaint, Owner

class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner',)
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town', 'owner_pure_phone')
    list_editable = ('new_building',)
    # list_display_links = ('owner',)
    readonly_fields = ('created_at',)
    list_filter = ('new_building', 'rooms_number', 'floor', 'has_balcony')
    raw_id_fields = ('likes', )

class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('text',)
    raw_id_fields = ('user', 'flat')


class OwnerAdmin(admin.ModelAdmin):

    raw_id_fields = ('flat', )



admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
