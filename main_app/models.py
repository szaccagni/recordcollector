from django.db import models
from django.urls import reverse

CURRENCIES = (
    ('USD', 'US Dollars'),
    ('EUR', 'Euro'),
    ('GBP', 'British Pound Sterling')
)

class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('genres_index')

class Seller(models.Model):
    soldBy = models.CharField('name', max_length=200)

    def __str__(self):
        return self.soldBy

    def get_absolute_url(self):
        return reverse('sellers_index')

class Record(models.Model):
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    released = models.DateField()
    sellers = models.ManyToManyField(Seller, through='Price')
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return f'{self.artist} - {self.album}'

    def get_absolute_url(self):
        return reverse('detail',kwargs={'record_id': self.id})

class Price(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=2)
    currency = models.CharField(
        max_length=3,
        choices=CURRENCIES,
        default=CURRENCIES[0][0]
    )
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    record = models.ForeignKey(Record, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.seller} is selling {self.record} for {self.price} {self.currency}'
    
    def get_absolute_url(self):
        return reverse('sellers_detail', kwargs={'pk':self.seller.id})

class Review(models.Model):
    createdDate = models.DateField(auto_now_add=True)
    lastModified = models.DateField(auto_now=True)
    review = models.CharField(max_length=500)
    rating = models.IntegerField()
    record = models.ForeignKey(Record, on_delete=models.CASCADE)

class Photo(models.Model):
    url = models.CharField(max_length=200)
    record = models.ForeignKey(Record, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for record_id: {self.record_id} @{self.url}"