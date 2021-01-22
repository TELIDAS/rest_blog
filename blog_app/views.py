from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from blog_app.models import Post
from blog_app.serializers import PostSerializer


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