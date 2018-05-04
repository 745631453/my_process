import random
import time

from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from uauth.models import Users


def regist(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    if request.method == 'POST':
        # 获取注册信息
        name = request.POST.get('name')
        pa = request.POST.get('password')
        if Users.objects.filter(u_name=name).exists():
            return render(request, 'register.html', {'name': '用户存在'})
        else:
            password = make_password(pa)
            Users.objects.create(
                u_name=name,
                u_password=password
            )
            return HttpResponseRedirect('/uau/lo/')


def login(request):
    if request.method == 'GET':
        return render(request, 'day6_login.html')

    if request.method == 'POST':
        # 登陆成功，绑定参数到coolie中 set_cookie
        name = request.POST.get('name')
        pa = request.POST.get('password')

        if Users.objects.filter(u_name=name).exists():
            uname = Users.objects.get(u_name=name)
            if check_password(pa, uname.u_password):
                ticket = ''
                for _ in range(15):
                    s = 'abcdefghijklmnopqrstuvwxyz'
                    # 获取随机字符串
                    ticket += random.choice(s)
                now_time = int(time.time())
                ticket = ticket + str(now_time)
                # 绑定令牌到coolie（浏览器）
                reponse = HttpResponseRedirect('/st/index/')
                # max_age表示存在时间——秒
                reponse.set_cookie('ticket', ticket, max_age=30000)
                # 存服务器中
                uname.u_ticket = ticket
                uname.save()
                return reponse  # 存在浏览器中  后面才能直接get到
            else:
                # return HttpResponse('密码错误')
                return render(request, 'day6_login.html', {'password': '密码错误'})
        else:
            # return HttpResponse('不存在')
            return render(request, 'day6_login.html', {'name': '用户名不存在'})


# 删除ticket返回登录页面（退出登录）
def logout(request):
    if request.method == 'GET':
        reponse = HttpResponseRedirect('/uau/lo/')
        reponse.delete_cookie('ticket')
        return reponse


# 自带的验证方式
def djlogin(request):
    if request.method == 'GET':
        return render(request, 'longin.html')

    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        # 验证用户密码和账户，通过的话返回user对象
        u = auth.authenticate(username=name, password=password)
        if u:
            # 验证成功
            auth.login(request, u)
            return HttpResponseRedirect('/st/index/')
        else:
            return render(request, 'longin.html')


# 注册
def djregist(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        User.objects.create_user(username=name, password=password)

        return HttpResponseRedirect('/uau/djlo/')


# 退出
def djout(request):
    if request.method == 'GET':
        auth.logout(request)
        return HttpResponseRedirect('/uau/djlo/')