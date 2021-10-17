from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from movies.models import Movie
# Create your models here.

# RATE_CHOICES = [
#         (1, 'one'),
#         (2, 'tow'),
#         (3, 'three'),
#         (4, 'four'),
#         (5, 'five'),
#     ]


class Comment(models.Model):
    passage = models.CharField(max_length=200, null=False, blank=False)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    movie = models.ForeignKey(to=Movie, on_delete=models.CASCADE, related_name='comments')
    creat_timestamp = models.DateTimeField(auto_now_add=True)
    modify_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} - {self.rating}'
