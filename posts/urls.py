from django.urls import path

from .views import PostView, TopicView

app_name = 'posts'

urlpatterns = [
    path('posts/', PostView.as_view()),
    path('topics/', TopicView.as_view())
]