from django.urls import path
from .views import admin_view, send_email_view, long_running_operation_view, PostListCreateView, PostDetailView, CommentListCreateView, CommentDetailView, post_list


urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
    path('post_list/', post_list, name='post-list'),
    path('send_email/', send_email_view, name='send-email'),
    path('long_running_operation/', long_running_operation_view, name='long-running-operation'),
    path('top-admin/', admin_view, name='admin_view'),
]