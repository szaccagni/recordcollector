from django.shortcuts import render

records = [
    {'artist': 'Mac Miller', 'album': 'Circles', 'released': 'May 29, 2020'},
    {'artist': 'Nirvana', 'album': 'Incesticide', 'released': 'December 15, 1992'},
    {'artist': 'Queen', 'album': 'A Day at the Races', 'released': 'December 10, 1976'},
    {'artist': 'David Bowie', 'album': 'Hunky Dory', 'released': 'December 17, 1971'}
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def records_index(request):
    return render(request, 'records/index.html', {
        'records': records
    })