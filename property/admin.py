from django.contrib import admin

from .models import Flat

class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner')
    list_display = ('town', 'address', 'owner')
    list_display_links = ('owner',)
    readonly_fields = ('created_at',)


admin.site.register(Flat, FlatAdmin)

