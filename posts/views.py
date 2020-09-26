from django.shortcuts import render

from rest_framework import generics, permissions

from .models import Post
from .serializers import PostSerializer



class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    #who have permission to call this api
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)