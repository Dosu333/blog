from django.contrib import admin

from .models import Topic, Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    ordering = ['created_at']
    list_filter = ['category',]
    search_fields = ['title']

class TopicAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(Topic, TopicAdmin)
admin.site.register(Post, PostAdmin)