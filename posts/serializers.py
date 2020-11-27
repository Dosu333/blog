from rest_framework import serializers

from . import models

class TopicSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Topic
        fields = ('__all__')

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Post
        fields = ('__all__')

class CommentSerializer(serializers.ModelSerializer):
     class Meta:
         model = models.Comment
         fields = ('related_post','author','body')