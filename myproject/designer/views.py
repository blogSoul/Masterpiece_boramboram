from django.shortcuts import render

# Create your views here.

def designerhome(request):
    return render(request, 'designer/designerhome.html')

def detail(request):
    return render(request, 'designer/detail.html')