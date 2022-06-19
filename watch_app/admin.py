from django.contrib import admin
from watch_app.models import UserProfile


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user']}),
        ('Bio', {'fields': ['bio']}),
        ('Phone', {'fields': ['phone']}),
        ('Block', {'fields': ['block']}),
        # ('Neighborhood', {'fields': ['neighborhood']}),
        ('Photo', {'fields': ['photo']}),
    ]
    
admin.site.register(UserProfile, ProfileAdmin)