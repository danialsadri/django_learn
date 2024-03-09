from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from .serializers import (PostListSerializer, PostDetailSerializer,
                          PostUpdateSerializer, PostCreateSerializer)
from ...models import Post


# =================================================================================================================
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def post_list(request):
    posts = Post.objects.filter(status=True)
    serializer = PostListSerializer(instance=posts, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def post_detail(request, pk):
    post = get_object_or_404(Post, id=pk, status=True)
    serializer = PostDetailSerializer(instance=post)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_create(request):
    serializer = PostCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(data=serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def post_update(request, pk):
    post = get_object_or_404(Post, id=pk, status=True)
    serializer = PostUpdateSerializer(instance=post, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def post_delete(request, pk):
    post = get_object_or_404(Post, id=pk, status=True)
    post.delete()
    return Response({'message': 'item removed successfully'}, status=status.HTTP_204_NO_CONTENT)


# =================================================================================================================


# =================================================================================================================
class PostListView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostListSerializer

    def get(self, request):
        posts = Post.objects.filter(status=True)
        serializer = self.serializer_class(instance=posts, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class PostDetailView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostDetailSerializer

    def get(self, request, pk):
        post = get_object_or_404(Post, id=pk, status=True)
        serializer = self.serializer_class(instance=post)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class PostCreateView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostCreateSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class PostUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostUpdateSerializer

    def patch(self, request, pk):
        post = get_object_or_404(Post, id=pk, status=True)
        serializer = self.serializer_class(instance=post, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)


class PostDeleteView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = None

    def delete(self, request, pk):
        post = get_object_or_404(Post, id=pk, status=True)
        post.delete()
        return Response({'message': 'item removed successfully'}, status=status.HTTP_204_NO_CONTENT)


# =================================================================================================================


# =================================================================================================================
# class PostListCreateView(GenericAPIView):
#     queryset = Post.objects.filter(status=True)
#     serializer_class = PostListSerializer
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request):
#         queryset = self.get_queryset()
#         serializer = self.serializer_class(instance=queryset, many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(data=serializer.data, status=status.HTTP_201_CREATED)


# class PostListCreateView(GenericAPIView, ListModelMixin, CreateModelMixin):
#     queryset = Post.objects.filter(status=True)
#     serializer_class = PostListSerializer
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


class PostListCreateView(ListCreateAPIView):
    queryset = Post.objects.filter(status=True)
    serializer_class = PostListSerializer
    permission_classes = [IsAuthenticated]


# =================================================================================================================
# class PostRetrieveUpdateDetailView(GenericAPIView):
#     serializer_class = PostDetailSerializer
#     permission_classes = [IsAuthenticated]
#     lookup_field = 'id'
#     lookup_url_kwarg = 'post_id'
#
#     def get_object(self):
#         pk = self.kwargs.get('post_id')
#         return get_object_or_404(Post, id=pk, status=True)
#
#     def get(self, request, *args, **kwargs):
#         post = self.get_object()
#         serializer = self.serializer_class(instance=post)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#     def patch(self, request, *args, **kwargs):
#         post = self.get_object()
#         serializer = self.serializer_class(instance=post, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
#
#     def delete(self, request, *args, **kwargs):
#         post = self.get_object()
#         post.delete()
#         return Response({'message': 'item removed successfully'}, status=status.HTTP_204_NO_CONTENT)


# class PostRetrieveUpdateDetailView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     serializer_class = PostDetailSerializer
#     permission_classes = [IsAuthenticated]
#     lookup_field = 'id'
#     lookup_url_kwarg = 'post_id'
#
#     def get_object(self):
#         pk = self.kwargs.get('post_id')
#         return get_object_or_404(Post, id=pk, status=True)
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def patch(self, request, *args, **kwargs):
#         return self.partial_update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


class PostRetrieveUpdateDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = PostDetailSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    lookup_url_kwarg = 'post_id'

    def get_object(self):
        pk = self.kwargs.get('post_id')
        return get_object_or_404(Post, id=pk, status=True)
# =================================================================================================================
