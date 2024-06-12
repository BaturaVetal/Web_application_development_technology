from django.urls import path
from .views import CustomUserCreateView, CustomUserDetailView, users_status

urlpatterns = [
    path('register/', CustomUserCreateView.as_view(), name='user-register'),
    path('profile/<int:pk>/', CustomUserDetailView.as_view(), name='user-detail'),
    path('status/', users_status, name='users-status'),
]
