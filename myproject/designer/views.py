from django.shortcuts import render, get_object_or_404
from .models import Art

def designerhome(request):
    arts = Art.objects
    return render(request, 'designer/designerhome.html', {'Arts': arts})

def detail(request, Art_id):
    Art_detail = get_object_or_404(Art, pk=Art_id)
    return render(request, 'designer/detail.html', {'ArtDetail': Art_detail})