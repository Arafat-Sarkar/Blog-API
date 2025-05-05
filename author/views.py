from django.shortcuts import render
from .import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins, viewsets
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.shortcuts import redirect
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator



class UserRegistrationApiView(APIView):
    serializer_class = serializers.RegistrationSerializer
    permission_classes = [AllowAny] 
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            return Response("User registered successfully")
        return Response(serializer.errors)

@method_decorator(csrf_exempt, name='dispatch')
class UserLoginApiView(APIView):
    serializer_class = serializers.UserLoginSerializer
    permission_classes = [AllowAny]  
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username, password=password)

            if user:
                refresh = RefreshToken.for_user(user)
                login(request, user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'user_id': user.id
                }, status=status.HTTP_200_OK)
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserLogoutView(APIView):
    def get(self, request):
        logout(request)
        return redirect('login')