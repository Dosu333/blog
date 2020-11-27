from django.shortcuts import render

from rest_framework import generics, viewsets
from rest_framework import filters

from .models import Post, Topic, Comment
from .serializers import PostSerializer, TopicSerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['category__name']
    http_method_names = ['get']
    
    def get_queryset(self):
        return self.queryset.order_by('-created_at')

class TopicView(generics.ListAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

class CommentView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['related_post__id']

    def get_queryset(self):
        return self.queryset.order_by('-created_at')
