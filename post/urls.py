from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter() 
router.register('post', views.PostViewstes ) 

urlpatterns = [
    path('', include(router.urls)),
]