from django.contrib import admin

from .models import Topic, Post, Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    ordering = ['created_at']
    list_filter = ['category',]
    search_fields = ['title']

class TopicAdmin(admin.ModelAdmin):
    search_fields = ['name']

class CommentAdmin(admin.ModelAdmin):
    list_filter = ['related_post']

admin.site.register(Topic, TopicAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)