from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    body=models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_template', args=[str(self.id)])

class User(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    # password=models.CharField(max_length=50)


    def __str__(self):
        return self.first_name
    
    def get_absolute_url(self):
        return reverse('user', args=[str(self.id)])



