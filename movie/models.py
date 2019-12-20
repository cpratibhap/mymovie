from django.db import models


class Movie(models.Model):
    mid = models.CharField(max_length=20)
    title = models.CharField(max_length=100)

    class Meta:
        db_table = "movie"
