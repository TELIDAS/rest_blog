"""rest_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from blog_app.views import CommentViewSet, CommentViewSetDetail
from blog_app_2 import views as articles
from blog_app import views
from lesson3 import views as news
from knox import views as knox_views
from blog_app.views import LoginAPI
from django.urls import path

router = DefaultRouter()
router.register('', CommentViewSet, basename='comment')
router.register('', CommentViewSetDetail, basename='comment_detail')




urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

    path('api/register/', views.RegisterAPI.as_view(), name='register'),

    path('api/v1/posts-api/', views.PostAPIView.as_view()),
    path('api/v1/posts-api/<int:id>/', views.PostAPIViewDetail.as_view()),

    path('api/v1/posts-api/<int:id>/comments/', include(router.urls)),
    path('api/v1/posts-api/<int:id>/comments/', include(router.urls)),

    path('api/v1/articles/', articles.ArticleAPIView.as_view()),
    path('api/v1/articles/<int:id>/', articles.article_detail),


    path('api/v1/news/', news.NewsAPIView.as_view()),
    path('api/v1/news/<int:id>/', news.NewsItemView.as_view()),


]
