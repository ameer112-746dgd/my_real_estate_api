from django.contrib import admin
from .models import Property

# Register your models here.

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'createdAt', 'noRooms', 'noBath', 'size')
    search_fields = ('name', 'address', 'description')
    list_filter = ('price', 'noRooms', 'noBath')

admin.site.register(Property, PropertyAdmin)
