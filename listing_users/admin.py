from django.contrib import admin
from .models import ListingUser

# Register your models here.

class ListingUserAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'phone_number', 'topic')
    search_fields = ('firstname', 'lastname', 'email', 'phone_number')
    list_filter = ('topic',)

admin.site.register(ListingUser, ListingUserAdmin)
