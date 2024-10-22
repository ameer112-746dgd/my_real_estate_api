from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserAdmin(BaseUserAdmin):
    # Fields to display in the admin list view
    list_display = ('email', 'first_name', 'last_name', 'role', 'is_active', 'is_staff')
    
    # Fields to use in the search box in the admin view
    search_fields = ('email', 'first_name', 'last_name')

    # Fields to filter by in the admin list view
    list_filter = ('is_staff', 'is_active', 'role')

    # Fields to be displayed in the edit page for each user in the admin
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('role', 'is_active', 'is_staff', 'is_superuser')}),
        ('Important Dates', {'fields': ('last_login',)}),
    )

    # Fields for adding a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'role', 'is_active', 'is_staff', 'is_superuser'),
        }),
    )

    # Tell the admin which field is the unique identifier (email in this case)
    ordering = ('email',)
    filter_horizontal = ()

# Register the custom User model with the custom UserAdmin
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
