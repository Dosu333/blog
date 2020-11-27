from django.urls import path

from .views import PostViewSet, TopicView, CommentView

from rest_framework import routers 

app_name = 'posts'

router = routers.DefaultRouter()

router.register('posts', PostViewSet)

urlpatterns = [
    path('topics/', TopicView.as_view()),
    path('comments/', CommentView.as_view()),
]

urlpatterns += router.urls