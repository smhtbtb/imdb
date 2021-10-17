from django.contrib.auth.models import User
from django.db import models
from movies.models import Movie
# Create your models here.

RATE_CHOICES = [
        (1, 'one'),
        (2, 'tow'),
        (3, 'three'),
        (4, 'four'),
        (5, 'five'),
    ]


class Comment(models.Model):
    passage = models.CharField(max_length=200, null=True, blank=True)
    rating = models.CharField(max_length=2, choices=RATE_CHOICES)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    movie = models.ForeignKey(to=Movie, on_delete=models.CASCADE)
    creat_timestamp = models.DateTimeField(auto_now_add=True)
    modify_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} - {self.rating}'
