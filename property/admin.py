from django.contrib import admin

from .models import Flat

class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner',)
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town',)
    list_editable = ('new_building',)
    # list_display_links = ('owner',)
    readonly_fields = ('created_at',)


admin.site.register(Flat, FlatAdmin)

