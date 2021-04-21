from django.contrib import admin

from .models import Profile
# Register your models here.

class profileAdmin(admin.ModelAdmin):
    
    list_dispaly = [
        'name',
        'age',
        'address',
        'image'
    ]
    
admin.site.register(Profile, profileAdmin)