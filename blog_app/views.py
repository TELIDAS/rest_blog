from rest_framework import status, viewsets, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from blog_app.models import Post, Comment
from blog_app.serializers import PostSerializer, CommentSerializer


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



