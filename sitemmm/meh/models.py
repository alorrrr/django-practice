from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.CharField(max_length=7)
    about = models.TextField()
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    author_url = models.CharField(max_length=100, blank=True, editable=False)

    def save(self, *args, **kwargs):
        self.author_url = self.author.replace(" ", "_")
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('user-books', kwargs={'pk': self.username.username})

    def __str__(self):
        return f'{self.username} - {self.title}'
    
