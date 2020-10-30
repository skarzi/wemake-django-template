from django.contrib import admin

from server.apps.main.models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    """Admin panel example for ``BlogPost`` model."""
