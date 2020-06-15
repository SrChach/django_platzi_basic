"""User admin classes"""

# Django
from django.contrib import admin

# Custom model
from users.models import Profile

# admin.site.register(Profile)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin."""

    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    list_display_links = ('user',)
    list_editable = ('phone_number', 'website', 'picture')

    search_fields = (
        'user__username',
        'user__email',
        'user__first_name',
        'user__last_name',
        'phone_number'
    )

    list_filter = (
        'user__is_active',
        'user__is_staff',
        'created',
        'modified'
    )
