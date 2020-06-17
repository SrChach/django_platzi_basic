"""Post admin classes."""

# Django
from django.contrib import admin

# Posts model
from posts.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post in Admin view."""

    list_display = ('user', 'title', 'photo')
    list_display_links = ('title',)
    list_editable = ('photo',)

    search_fields = (
        'user__username',
        'user__first_name',
        'user__last_name',
        'title'
    )

    list_filter = (
        'created',
        'modified',
        'user__username'
    )
