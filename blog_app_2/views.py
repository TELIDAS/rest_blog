from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from blog_app_2.models import Article
from blog_app_2.serializers import ArticleSerializer


@api_view(['GET', 'POST'])
def article_view(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        return Response(data=ArticleSerializer(articles,
                                               many=True).data)
    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        article = Article.objects.create(title=title,
                                         description=description)
        article.save()
        return Response(data=ArticleSerializer(article).data,
                        status=status.HTTP_201_CREATED)


@api_view(["DELETE", 'PUT'])
def article_detail(request, id):
    article = Article.objects.get(id=id)

    if request.method == 'DELETE':
        article.delete()
        articles = Article.objects.all()
        return Response(data=ArticleSerializer(articles,
                                               many=True).data)

    elif request.method == 'PUT':
        title = request.data.get('title')
        description = request.data.get('description')
        article.title = title
        article.description = description
        article.save()

        return Response(data=ArticleSerializer(article).data,
                        status=status.HTTP_201_CREATED)


class ArticleAPIView(APIView):
    allow_methods = ['GET', 'POST']
    serializer_class = ArticleSerializer

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        return Response(data=self.serializer_class(articles,
                                                   many=True).data)


    def post(self, request, *args, **kwargs):
        title = request.data.get('title')
        description = request.data.get('description')
        article = Article.objects.create(title=title,
                                         description=description)
        article.save()
        return Response(data=self.serializer_class(article).data,
                        status=status.HTTP_201_CREATED)
