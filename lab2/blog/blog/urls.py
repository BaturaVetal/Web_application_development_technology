from django.urls import path
from .views import PostListCreateView, PostDetailView, CommentListCreateView, CommentDetailView, post_list

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
    path('post_list/', post_list, name='post-list'),
]
