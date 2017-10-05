from django.shortcuts import render
from third_app.forms import FormName

# Create your views here.

def index(request):
    return render(request, 'third_app/index.html')

def form_name_view(request):
    if request.method == 'POST':
        form = FormName(request.POST)

        if (form.is_valid()):
            print(form.cleaned_data)
    elif request.method == 'GET':
        form = FormName()

    return render(request, 'third_app/form_page.html', {'form': form})
