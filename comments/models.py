from django.contrib.auth.models import User
from django.db import models
from movies.models import movie
# Create your models here.

rate_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


class comments(models.Model):
    passage = models.CharField(max_length=200, null=True, blank=True)
    rating = models.CharField(max_length=2, choices=rate_list)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    movie = models.ForeignKey(to=movie, on_delete=models.CASCADE)
    creat_timestamp = models.DateTimeField(auto_now_add=True)
    modify_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} - {self.rating}'
