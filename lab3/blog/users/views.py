from datetime import timedelta

from django.utils import timezone
from rest_framework import generics
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render


class CustomUserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


def users_status(request):
    online_threshold = timezone.now() - timedelta(minutes=5)
    online_users = CustomUser.objects.filter(last_login__gte=online_threshold)
    offline_users = CustomUser.objects.filter(last_login__lt=online_threshold) | CustomUser.objects.filter(
        last_login__isnull=True)
    return render(request, 'users/users_status.html', {'online_users': online_users, 'offline_users': offline_users})


class CustomUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]


class UserProfileView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]
