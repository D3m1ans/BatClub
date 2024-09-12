from django.shortcuts import render

# Create your views here.

def index(request):
    data = {
        'title': 'BatClub',
    }
    return render(request, 'main/index.html', data)