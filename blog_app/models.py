from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, null=True)
    images = models.ImageField(upload_to='api/v1/posts/', null=True)
    description = models.TextField(null=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    def view_comments(self):
        return Comment.objects.filter(comments=self)



class Comment(models.Model):
    comment = models.TextField(null=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    post = models.ForeignKey(Post,
                             on_delete=models.SET_NULL,
                             null=True,
                             related_name='comments')
