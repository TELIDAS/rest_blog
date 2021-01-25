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
from django.urls import path
from blog_app_2 import views as articles
from blog_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/posts/', views.get_all_posts),
    path('api/v1/posts/<int:id>/', views.get_post),

    path('api/v1/articles/', articles.article_view),
    path('api/v1/articles/<int:id>/', articles.article_detail),

]
