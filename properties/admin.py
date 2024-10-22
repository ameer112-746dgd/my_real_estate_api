from django.contrib import admin
from .models import Property

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'formatted_price', 'createdAt', 'noRooms', 'noBath', 'size')
    search_fields = ('name', 'address', 'description')
    list_filter = ('price', 'noRooms', 'noBath', 'currency')

    def formatted_price(self, obj):
            return f"{obj.currency} {obj.price}"
    formatted_price.short_description = 'Price'

admin.site.register(Property, PropertyAdmin)
