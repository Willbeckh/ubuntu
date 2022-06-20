from django.contrib import admin
from watch_app.models import UserProfile, Neighborhood, Facility


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user']}),
        ('Bio', {'fields': ['bio']}),
        ('Phone', {'fields': ['phone']}),
        ('Street', {'fields': ['street']}),
        ('Neighborhood', {'fields': ['neighborhood']}),
        ('Location', {'fields': ['location']}),
        ('Photo', {'fields': ['photo']}),
    ]
    
admin.site.register(UserProfile, ProfileAdmin)

class NeighborhoodAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Location', {'fields': ['location']}),
        ('Occupants', {'fields': ['occupants']}),
        ('User', {'fields': ['user']}),
        ('Facilities', {'fields': ['facilities']}),
        # ('Business', {'fields': ['business']}),
    ]
    
admin.site.register(Neighborhood, NeighborhoodAdmin)


class FacilityAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ('email', {'fields': ['email']}),
        ('phone', {'fields': ['contact']}),
        ('location', {'fields': ['location']}),
        ('Picture', {'fields': ['picture']}),
    ]
    
admin.site.register(Facility, FacilityAdmin)