from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')
# 아직 완성 안되었습니다. 확인요망