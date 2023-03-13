from django.contrib import admin

from .models import Flat

class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'id', 'owner')
    list_display = ('address', 'price', 'construction_year', 'town', )
    readonly_fields = ('created_at',)



admin.site.register(Flat, FlatAdmin)