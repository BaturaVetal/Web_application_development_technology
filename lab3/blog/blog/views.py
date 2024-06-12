from rest_framework import generics, filters
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import render
from django.http import JsonResponse
from .tasks import send_email_task, long_running_task


def admin_view(request):
    return render(request, 'admin.html')


def send_email_view(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        emails = ['batura.vitaliy@lll.kpi.ua']

        if subject and message:
            send_email_task.delay(subject, message, emails)
            return JsonResponse({'status': 'Email sent'})
        else:
            return JsonResponse({'error': 'Subject and message are required'}, status=400)

    return render(request, 'send_email.html')


def long_running_operation_view(request):
    if request.method == 'POST':
        operation_data = request.POST.get('operation_data')

        if operation_data:
            long_running_task.delay(operation_data)
            return JsonResponse({'status': 'Long running operation started'})
        else:
            return JsonResponse({'error': 'Operation data is required'}, status=400)

    return render(request, 'long_running_operation.html')


def post_list(request):
    return render(request, 'blog/post_list.html')


class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content']
    ordering_fields = ['created_at']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['content']
    ordering_fields = ['created_at']


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
