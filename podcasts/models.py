from django.db import models


class Episode(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    publication_date = models.DateTimeField()
    link = models.URLField()
    image = models.URLField()
    podcast_name = models.CharField(max_length=100)
    unique_attribute = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.podcast_name}: {self.title}'

