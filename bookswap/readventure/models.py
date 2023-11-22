from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

# class Book(models.Model):
#     title = models.CharField(max_length=255)
#     author = models.CharField(max_length=255)
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)

