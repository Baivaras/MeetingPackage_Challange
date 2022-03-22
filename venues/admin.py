from django.contrib import admin

from venues.models import Venue


@admin.register(Venue)
class VenuesAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'country', 'latitude', 'longitude', 'created_at', 'updated_at')
    list_filter = ('city', 'country')
    search_fields = ('name', 'city', 'country')
