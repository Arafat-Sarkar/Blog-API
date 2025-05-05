
from rest_framework import serializers
from .models import PostModel


class PostSerializers(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        model = PostModel
        fields = ['id', 'title', 'content', 'author', 'image', 'created_at', 'updated_at']