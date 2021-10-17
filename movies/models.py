from django.db import models


# Create your models here.


class Movie(models.Model):
    """
    model of movies
    """

    name = models.CharField(max_length=30, null=False, blank=False)
    director = models.CharField(max_length=20, null=False, blank=False)
    description = models.CharField(max_length=200, null=True, blank=True)
    creat_timestamp = models.DateTimeField(auto_now_add=True)
    modify_timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-creat_timestamp',)

    def __str__(self):
        return f'{self.name} - {self.director}'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)



