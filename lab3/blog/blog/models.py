from users.models import CustomUser
from django.db import models


class LongRunningOperation(models.Model):
    operation_name = models.CharField(max_length=255)
    data = models.TextField()
    result = models.TextField(blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.operation_name



class Post(models.Model):
    objects = None
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
