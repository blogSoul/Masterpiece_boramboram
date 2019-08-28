from django.shortcuts import render, get_object_or_404, redirect
from .models import Servicecenter
from django.utils import timezone
# Create your views here.
def home(request):
    notices = Servicecenter.objects
    return render(request, 'servicecenter/home.html', {'notices': notices})

def detail(request, servicecenter_id):
    servicecenter_detail = get_object_or_404(Servicecenter, pk=servicecenter_id)
    return render(request, 'servicecenter/detail.html', {'notice': servicecenter_detail})

def write(request):
    return render(request, 'servicecenter/write.html')

def create(request):
    write = Servicecenter()
    write.title = request.GET['title']
    write.body = request.GET['body']
    write.pub_date = timezone.datetime.now()
    write.save()
    return redirect('/servicecenter/' + str(write.id))