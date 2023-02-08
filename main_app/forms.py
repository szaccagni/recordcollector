from django.forms import ModelForm
from .models import Review, Price

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields =['review', 'rating']

class PriceForm(ModelForm):
    class Meta:
        model = Price
        fields = ['price', 'currency', 'record']