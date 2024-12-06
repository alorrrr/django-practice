from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.CharField(max_length=7)
    about = models.TextField()
    username = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.username} - {self.title}'
