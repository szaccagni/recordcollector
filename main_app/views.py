from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Record
from .forms import ReviewForm

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