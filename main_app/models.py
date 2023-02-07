from django.db import models
from django.urls import reverse

class Seller(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=2)
    soldBy = models.CharField(max_length=200)

    def __str__(self):
        return self.soldBy


class Record(models.Model):
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    released = models.DateField()
    sellers = models.ManyToManyField(Seller)

    def __str__(self):
        return f'{self.artist} - {self.album}'

    def get_absolute_url(self):
        return reverse('detail',kwargs={'record_id': self.id})

class Review(models.Model):
    createdDate = models.DateField(auto_now_add=True)
    lastModified = models.DateField(auto_now=True)
    review = models.CharField(max_length=500)
    rating = models.IntegerField()
    record = models.ForeignKey(Record, on_delete=models.CASCADE)