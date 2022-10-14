from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from .models import User
from django.contrib.auth import get_user_model #사용자가 있는지 검사하는 함수
from django.contrib import auth # 사용자 auth 기능


# Create your views here.
def signup(request):
    if request.method == "GET":
        user = request.user.is_authenticated # 로그인 된 사용자가 요청하는지 검사
        if user: # 로그인이 되어있다면
            return redirect('/')
        else: # 로그인이 되어있지 않다면
            return render(request, 'user/account/signup.html')
            
    elif request.method == "POST":
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        passwordcheck = request.POST.get('passwordcheck')
        if password != passwordcheck:
            # User.objects.create_user(username = username, password = password)
            return redirect('user/account/signup.html') 
        else:
            exist_user = get_user_model().objects.filter(username=username)
            if exist_user:
                return render(request, 'user/account/signup.html') # 사용자가 존재하기 때문에 사용자를 저장하지 않고 회원가입 페이지를 다시 띄움
            else:
                User.objects.create_user(username=username, password=password)
                return redirect('/account/signin') # 회원가입이 완료되었으므로 로그인 페이지로 이동

def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return redirect('/account/signin')  # 로그인 실패
    elif request.method == 'GET':
        user = request.user.is_authenticated # 로그인 된 사용자가 요청하는지 검사
        if user: # 로그인이 되어있다면
            return redirect('/')
        else: # 로그인이 되어있지 않다면
            return render(request, 'user/account/login.html')

@login_required
def logout(request):
    auth.logout(request) # 인증 되어있는 정보를 없애기
    return redirect("/")



