from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    


class Pd(models.Model):

    author = models.CharField(max_length=200, default='string')
    bookname = models.CharField(max_length=200, default='string')
    published_date = models.DateTimeField(blank=True, null=True)
    text = models.TextField(default=True)

    def __str__(self):
        return self.bookname

class Nonfiction(models.Model):

    author = models.CharField(max_length=200, default='string')
    bookname = models.CharField(max_length=200, default='string')
    published_date = models.DateTimeField(blank=True, null=True)
    text = models.TextField(default=True)

    def __str__(self):
        return self.bookname

class Mysteries(models.Model):
    author = models.CharField(max_length=200, default='string')
    bookname = models.CharField(max_length=200, default='string')
    published_date = models.DateTimeField(blank=True, null=True)
    text = models.TextField(default=True)

    def __str__(self):
        return self.bookname

class Romance(models.Model):
    author = models.CharField(max_length=200, default='string')
    bookname = models.CharField(max_length=200, default='string')
    published_date = models.DateTimeField(blank=True, null=True)
    text = models.TextField(default=True)

    def __str__(self):
        return self.bookname

class Biography(models.Model):
    author = models.CharField(max_length=200, default='string')
    bookname = models.CharField(max_length=200, default='string')
    published_date = models.DateTimeField(blank=True, null=True)
    text = models.TextField(default=True)

    def __str__(self):
        return self.bookname

    
    

