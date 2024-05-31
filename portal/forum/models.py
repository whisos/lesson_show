from django.db import models
from django.contrib.auth.models import User


class Forum_Theme(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

class Forum_post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    #media
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    theme = models.ForeignKey(Forum_Theme, on_delete=models.CASCADE, related_name='themes')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    post = models.ForeignKey(Forum_post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    media = models.FileField(upload_to='comments_media/',blank = True, null =True)

    def get_absolute_url(self):
        return self.post.get_absolute_url()

class Like(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked_comments')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('comment', 'user')
