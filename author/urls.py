from django.urls import path
from .views import UserRegistrationApiView,UserLoginApiView,UserLogoutView


urlpatterns = [
    path('register/', UserRegistrationApiView.as_view()),
     path('login/', UserLoginApiView.as_view(), name='login'),
     path('logout/', UserLogoutView.as_view()),
]

