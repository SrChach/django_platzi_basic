"""User admin classes"""

# Django
from django.contrib import admin

# Custom model
from users.models import Profile

# admin.site.register(Profile)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin."""

    list_display = ('user', 'phone_number', 'website')
