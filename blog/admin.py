from django.contrib import admin
from .models import Post


class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'text', 'created_date', 'published_date',)
    list_editable = ('text',)
    list_display_links = ('id', 'title', 'published_date',)

admin.site.register(Post, ComentarioAdmin)
