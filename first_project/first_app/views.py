from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    params = {'insert_me': 'Hello i\'m from views.py!'}
    return render(request, 'first_app/index.html', context=params)

def fox(request):
    return render(request, 'first_app/fox.html')
