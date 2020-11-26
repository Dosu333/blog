from django.shortcuts import render

from rest_framework.generics import ListAPIView
from rest_framework import filters

from .models import Post, Topic
from .serializers import PostSerializer, TopicSerializer

class PostView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['category__name']
    
    def get_queryset(self):
        return self.queryset.order_by('-created_at')

class TopicView(ListAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer