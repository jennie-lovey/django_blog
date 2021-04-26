from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=200)
    author=models.ForeignKey('auth.user', on_delete=models.CASCADE)
    body=models.TextField()

    def __str__(self):
        return self.title
    
class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name ='comments')
  user = models.ForeignKey(User, on_delete = models.CASCADE)
  content = models.TextField()

  def __str__(self):
      return self.content