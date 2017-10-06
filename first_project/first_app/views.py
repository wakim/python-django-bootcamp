from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

from first_app.forms import UserForm
from first_app.models import *

# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dic = {'access_records': webpages_list}

    return render(request, 'first_app/index.html', date_dic)

def users(request):
    users = User.objects.order_by('id')
    params = {'users': users}

    return render(request, 'first_app/users.html', params)

def signup(request):
    if request.method == 'GET':
        form = UserForm()
    elif request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()

    return render(request, 'first_app/signup.html', {'form': form})
