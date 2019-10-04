from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import get_user_model

# Create your views here.

User = get_user_model()

def signup(request):
    '''
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user =User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'],
                user_realname=request.POST['realname'],
                email=request.POST['email'],
                user_phone_number=request.POST['phonenumber']
            )
            if user is None:
                auth.login(request, User)
                return redirect('home')
            else:
                return redirect('home')
    return render(request, 'accounts/signup.html')
    # 왜 안되는거야 ... ㅜㅡㅜ
    # 이 부분은 아이디 중복 기능이 없어서 주석처리해두었습니다.
    '''
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(
                    username=request.POST['username'],
                    password=request.POST['password1'],
                    user_realname=request.POST['realname'],
                    email=request.POST['email'],
                    user_phone_number=request.POST['phonenumber'],
                )
                return render(request, 'account/signup.html', {'error': 'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1'],
                    user_realname=request.POST['realname'],
                    email=request.POST['email'],
                    user_phone_number=request.POST['phonenumber'],
                )
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Passwords must match'})
    else:
        return render(request, 'accounts/signup.html')
    # try 구문으론 odject의 doesnotexit를 읽을 수 없다.
    # auth는 user 한명에게만 해당된다.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'accounts/signup.html')