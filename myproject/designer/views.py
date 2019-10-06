from django.shortcuts import render
from .models import Art

def designerhome(request):
    art = Art.objects
    return render(request, 'designer/designerhome.html', {'Art': art})

def detail(request):
    return render(request, 'designer/detail.html')