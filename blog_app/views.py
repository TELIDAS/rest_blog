from django.contrib.auth import login
from knox.models import AuthToken
from knox.views import LoginView
from rest_framework import status, viewsets, mixins, generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from blog_app.models import Post, Comment
from blog_app.serializers import PostSerializer, CommentSerializer, UserSerializer, RegisterSerializer

from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView


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
    allow_methods = ['DELETE', 'PUT', 'GET']
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


class CommentViewSet(viewsets.GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class CommentViewSetDetail(viewsets.GenericViewSet,
                           mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)