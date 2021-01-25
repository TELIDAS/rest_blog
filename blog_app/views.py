from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from blog_app.models import Post
from blog_app.serializers import PostSerializer


class PostAPIView(APIView):
    allow_methods = ['GET', 'POST']
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        return Response(data=self.serializer_class(posts,
                                                   many=True).data)

    def post(self, request, *args, **kwargs):
        title = request.data.get('title')
        description = request.data.get('description')
        post = Post.objects.create(title=title,
                                   description=description)
        post.save()
        return Response(data=self.serializer_class(post).data,
                        status=status.HTTP_201_CREATED)



class PostAPIViewDetail(APIView):
    allow_methods = ['DELETE', 'PUT']
    serializer_class = PostSerializer

    def get(self, request, id):
        post = Post.objects.get(id=id)
        return Response(data=self.serializer_class(post).data)


    def delete(self, request, *args, **kwargs):
        post = Post.objects.get(id=id)
        post.delete()
        posts = Post.objects.all()
        return Response(data=self.serializer_class(posts).data,
                        status=status.HTTP_200_OK)


    def put(self, request, id):
        post = Post.objects.get(id=id)
        title = request.data.get('title')
        description = request.data.get('description')
        post.title = title
        post.description = description
        post.save()

        return Response(data=self.serializer_class(post).data,
                        status=status.HTTP_200_OK)


@api_view(['GET'])
def get_all_posts(request):
    posts = Post.objects.all()
    data = PostSerializer(posts,
                          many=True).data
    return Response(data=data)


@api_view(['GET'])
def get_post(request, id):
    try:
        posts = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return Response(data={'result': 'post does not exist, baby'},
                        status=status.HTTP_404_NOT_FOUND)
    data = PostSerializer(posts).data
    return Response(data=data, status=status.HTTP_200_OK)