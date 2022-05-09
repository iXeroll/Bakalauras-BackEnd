from django.shortcuts import render
from paslaugos.models import Post
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import PostSerializer
from rest_framework.permissions import (
    SAFE_METHODS,
    BasePermission,
    IsAuthenticated,
    AllowAny,
)
from django.shortcuts import get_object_or_404
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser


class PostUserWritePermission(BasePermission):
    message = "Posts can only be edited by author"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user


## List Post
class PostList(viewsets.ModelViewSet):
    permission_classes = [PostUserWritePermission]
    serializer_class = PostSerializer
    # queryset = Post.postobjects.all()

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get("pk")
        return get_object_or_404(Post, id=item)

    def get_queryset(self):
        return Post.objects.filter(status="active").order_by("-updateDate")


# Post Search
class PostListSearch(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["@title", "@description"]


# Post CRUD


class UserPostDetails(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        item = self.kwargs.get("pk")
        return Post.objects.filter(author=item).order_by("-updateDate")


# class CreatePost(generics.CreateAPIView):
#     permission_classes = [PostUserWritePermission]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


class CreatePost(APIView):
    permission_classes = [AllowAny]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        print(request.data)
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdatePost(generics.UpdateAPIView):
    permission_classes = [AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class DeletePost(generics.RetrieveDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# class PostList(viewsets.ViewSet):
#     permission_classes = [IsAuthenticated]
#     queryset = Post.postobjects.all()

#     def list(self, request):
#         serializer_class = PostSerializer(self.queryset, many=True)
#         return Response(serializer_class.data)

#     def retrieve(self, requst, pk=None):
#         post = get_object_or_404(self.queryset, pk=pk)
#         serializer_class = PostSerializer(post)
#         return Response(serializer_class.data)


# # Create your views here.
# class PostList(generics.ListCreateAPIView):
#     queryset = Post.postobjects.all()
#     serializer_class = PostSerializer


# class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
#     permission_classes = [PostUserWritePermission]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


"""
#CreateAPIView
Used for create-only endpoints.
Provides a post method handler.
Extends: GenericAPIView, CreateModelMixin

#ListAPIView
Used for read-only endpoints to represent a collection of model instances.
Provides a get method handler.
Extends: GenericAPIView, ListModelMixin

#RetrieveAPIView
Used for read-only endpoints to represent a single model instance.
Provides a get method handler.
Extends: GenericAPIView, RetrieveModelMixin

#DestroyAPIView
Used for delete-only endpoints for a single model instance.
Provides a delete method handler.
Extends: GenericAPIView, DestroyModelMixin

#UpdateAPIView
Used for update-only endpoints for a single model instance.
Provides put and patch method handlers.
Extends: GenericAPIView, UpdateModelMixin

#ListCreateAPIView
Used for read-write endpoints to represent a collection of model instances.
Provides get and post method handlers.
Extends: GenericAPIView, ListModelMixin, CreateModelMixin

#RetrieveUpdateAPIView
Used for read or update endpoints to represent a single model instance.
Provides get, put and patch method handlers.
Extends: GenericAPIView, RetrieveModelMixin, UpdateModelMixin

#RetrieveDestroyAPIView
Used for read or delete endpoints to represent a single model instance.
Provides get and delete method handlers.
Extends: GenericAPIView, RetrieveModelMixin, DestroyModelMixin

#RetrieveUpdateDestroyAPIView
Used for read-write-delete endpoints to represent a single model instance.
Provides get, put, patch and delete method handlers.
Extends: GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
"""
