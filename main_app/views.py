from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView, DetailView
from .models import Record, Seller, Price
from .forms import ReviewForm, PriceForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def records_index(request):
    records = Record.objects.all()
    return render(request, 'records/index.html', {
        'records': records
    })

def records_detail(request, record_id):
    record = Record.objects.get(id=record_id)
    review_form = ReviewForm()
    return render(request, 'records/detail.html', {'record': record, 'review_form': review_form})

class RecordCreate(CreateView):
    model = Record
    fields = '__all__'

class RecordUpdate(UpdateView):
    model = Record
    fields = '__all__'

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