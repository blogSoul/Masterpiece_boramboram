from django.shortcuts import render, get_object_or_404
from .models import Servicecenter
# Create your views here.
def home(request):
    notices = Servicecenter.objects
    return render(request, 'servicecenter/home.html', {'notices': notices})

def detail(request, servicecenter_id):
    servicecenter_detail = get_object_or_404(Servicecenter, pk=servicecenter_id)
    return render(request, 'servicecenter/detail.html', {'notice': servicecenter_detail})