from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import SET_NULL, CASCADE


class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(User, null=True, on_delete=CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=SET_NULL,
                             null=True,
                             related_name='comments')
    text = models.TextField()