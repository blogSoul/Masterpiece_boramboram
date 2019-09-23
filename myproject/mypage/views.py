from django.shortcuts import render

# Create your views here.

def myinform(request):
    return render(request, 'mypage/myinform.html')

def myorder(request):
    return render(request, 'mypage/myorder.html')