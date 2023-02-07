from django.db import models
from django.urls import reverse

class Record(models.Model):
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    released = models.DateField()

    def __str__(self):
        return f'{self.artist} - {self.album}'

    def get_absolute_url(self):
        return reverse('detail',kwargs={'record_id': self.id})