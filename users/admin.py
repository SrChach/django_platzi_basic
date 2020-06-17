"""User admin classes"""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

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

    """
    List of categories with chich we'll create a 'Profile'

    It's a tuple of tuples. Each tuple must have as key the name of category
    that we'll assign to it. As value, a tuple with the fields to add.
    """
    fieldsets = (
        ('Profile', {
            'fields': (('user', 'picture'), ) # Rendered side by side
        }),
        ('Contact data', {
            'fields': ('phone_number', 'website', 'biography') # Rendered one below other
        }),
        ('Metadata', {
            'fields': (('created', 'modified'),)
        })
    )

    readonly_fields = ('created', 'modified')


class ProfileInline(admin.StackedInline):
    """Extending User on admin to edit User and Profile in-same-view."""

    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    """Overriding user admin's model with our own."""

    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
        'is_superuser'
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
