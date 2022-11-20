from django.urls import reverse
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateTimeField(default = timezone.now )
    view = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='post_like')
    Hashtags = TaggableManager()

    class Meta:
        ordering = ['-date']

    def get_absolute_url(self):
        return reverse("postdetail", args=[self.title])

    def number_of_views(self):
        return self.view

    def number_of_likes(self):
        return self.likes.count

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    commentator = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f'{self.commentator.username} commented on {self.post.title}'