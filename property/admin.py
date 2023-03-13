from django.contrib import admin

from .models import Flat, Complaint, Owner


class FlatInline(admin.TabularInline):
    model = Owner.flat.through
    raw_id_fields = ["owner", "flat"]
    extra = 1
    verbose_name = 'Собственник'
    verbose_name_plural = 'Собственники'



class FlatAdmin(admin.ModelAdmin):
    inlines = [FlatInline, ]
    search_fields = ('town', 'address', 'id', 'owner')
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town',)
    list_editable = ('new_building',)
    readonly_fields = ('created_at',)
    list_filter = ('new_building', 'rooms_number', 'floor', 'has_balcony')
    raw_id_fields = ('likes',)


class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('user', 'flat', 'text', )
    raw_id_fields = ('user', 'flat')


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat', )



admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)