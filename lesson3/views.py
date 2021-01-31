from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from lesson3.models import News, Comment
from lesson3.serializers import NewsSerializer, NewsCreateSerializer


class NewsAPIView(APIView):
    allow_methods = ['GET', 'POST']
    serializer_class = NewsSerializer

    def get(self, request, *args, **kwargs):
        news = News.objects.filter(author=request.user)
        return Response(data=self.serializer_class(news,
                                                   many=True).data)

    def post(self, request, *args, **kwargs):
        serializer = NewsCreateSerializer(data=request.data)
        if serializer.is_valid():
            news = News.objects.create(title=serializer.title,
                                       description=serializer.description)
            news.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

class NewsItemView(APIView):
    allow_methods = ['GET', 'POST']

    def get(self, request, id):
        news = News.objects.get(id=id)
        return Response(data=NewsSerializer(news).data)

    def post(self, request, id):
        news = News.objects.get(id=id)
        comment = request.data.get('comment')
        new_comment = Comment.objects.create(text=comment, news=news)
        new_comment.save()
        return Response(status=status.HTTP_201_CREATED)

class NewsViewSet(ModelViewSet):
    def list(self, request, *args, **kwargs):
        news = News.objects.all()
        return Response(data=self.serializer_class(news,
                                                   many=True).data)