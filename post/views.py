from django.shortcuts import render
from rest_framework import viewsets, permissions, pagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import PostModel
from .serializers import PostSerializers


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:
            return True

        
        return obj.author == request.user


class PostPagination(pagination.PageNumberPagination):
    page_size = 2 
    page_size_query_param = 'page_size'
    max_page_size = 100
    

class PostViewstes(viewsets.ModelViewSet):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializers
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    pagination_class = PostPagination
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)