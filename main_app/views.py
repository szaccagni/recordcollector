import uuid
import boto3
import os
from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView, DetailView
from .models import Record, Seller, Price, Photo
from .forms import ReviewForm, PriceForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html', {'activeLink': 'about', 'dataColor': '#0E0E0F'})

def records_index(request):
    records = Record.objects.all()
    return render(request, 'records/index.html', {
        'records': records,
        'activeLink' : 'records',
        'dataColor' : '#0E0E0F'
    })

def records_detail(request, record_id):
    record = Record.objects.get(id=record_id)
    review_form = ReviewForm()
    return render(request, 'records/detail.html', {'record': record, 'review_form': review_form})

class RecordCreate(CreateView):
    model = Record
    fields = ['artist', 'album', 'released']
    def get_context_data(self, **kwargs):
        context = super(RecordCreate, self).get_context_data(**kwargs)
        context['activeLink'] = 'records'
        context['dataColor'] = '#0E0E0F'
        return context

class RecordUpdate(UpdateView):
    model = Record
    fields = ['artist', 'album', 'released']

    def get_context_data(self, **kwargs):
        context = super(RecordUpdate, self).get_context_data(**kwargs)
        context['activeLink'] = 'records'
        context['dataColor'] = '#0E0E0F'
        return context

class RecordDelete(DeleteView):
    model = Record
    success_url = '/records'

def add_review(request, record_id):
    form = ReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.record_id = record_id
        new_review.save()
    return redirect('detail', record_id=record_id)

class SellerList(ListView):
    model = Seller
    template_name = 'main_app/vseller_list.html'
	
    def get_context_data(self, **kwargs):
        context = super(SellerList, self).get_context_data(**kwargs)
        context['activeLink'] = 'sellers'
        context['dataColor'] = '#FFE973'
        return context

class SellerDetail(DetailView):
    model = Seller

class SellerCreate(CreateView):
    model = Seller
    fields = '__all__'

class SellerUpdate(UpdateView):
    model = Seller
    fields = ['review', 'price']

class PriceCreate(CreateView):
    model = Price
    form_class = PriceForm

    def dispatch(self, request, *args, **kwargs):
        self.seller = get_object_or_404(Seller, pk=kwargs['seller_id'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.seller = self.seller
        return super().form_valid(form)

def add_photo(request, record_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, record_id=record_id)
        except Exception as e:
            print('Anerror occurred uplaodding file to S3')
            print(e)
    return redirect('detail', record_id=record_id)