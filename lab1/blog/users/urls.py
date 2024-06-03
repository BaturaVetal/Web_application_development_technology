from django.urls import path
from .views import CustomUserCreateView, CustomUserDetailView

urlpatterns = [
    path('register/', CustomUserCreateView.as_view(), name='user-register'),
    path('profile/<int:pk>/', CustomUserDetailView.as_view(), name='user-detail'),
]
