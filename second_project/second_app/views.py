from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('<html><body><em>My Second App</em></body></html>')

def help(request):
    params = {'help_insert': 'Looking for help?'}
    return render(request, 'second_app/help.html', context=params)
