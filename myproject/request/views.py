from django.shortcuts import render
from .models import Request

def requesthome(request):
    request_object = Request.objects
    return render(request, 'request/requesthome.html', {'Request_objects': request_object})

def explain(request):
    return render(request, 'request/explain.html')