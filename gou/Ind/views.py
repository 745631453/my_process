import random
from datetime import datetime, timedelta
import time
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from Ind.models import MainLun, MainDao, MainMustBuy, MainShop, MainShow, MinModel \
    , MineModel


# 首页展示
def Home(request):
    # 将数据库的的参数传到页面去展示，同时注意只展示一个或指定的几个的时候要么在数据库中切片
    # 要么在页面中forloop.counter函数定义
    if request.method == 'GET':
        lun = MainLun.objects.all()
        dao = MainDao.objects.all()
        buy = MainMustBuy.objects.all()
        shop = MainShop.objects.all()
        shop1 = MainShop.objects.all()[0]
        shop2 = list(MainShop.objects.all()[1:3])
        shop3 = list(MainShop.objects.all()[3:7])
        shop4 = list(MainShop.objects.all()[7:11])
        show = MainShow.objects.all()
        ttp = {
            'lun': lun,
            'dao': dao,
            'buy': buy,
            'shop': shop,
            'show': show,
            'shop1': shop1,
            'shop2': shop2,
            'shop3': shop3,
            'shop4': shop4,

        }

        return render(request, 'home/home.html', ttp)


# 登录页面
def Login(request):
    if request.method == 'GET':
        return render(request, 'user/user_login.html')
    if request.method == 'POST':
        nam = request.POST.get('username')
        passwor = request.POST.get('password')
        if MinModel.objects.filter(usernam=nam).exists():
            name = MinModel.objects.get(usernam=nam)
            if name.password == passwor:
                # 设置cookie值
                ticket = ''
                for _ in range(15):
                    a = 'abcdefghijklmnopqrstuvwxyz'
                    ticket += random.choice(a)
                ti = int(time.time())
                ticket += str(ti)
                re = HttpResponseRedirect('/ind/home/')
                # 设置失效时间
                out_time = datetime.now() + timedelta(days=1)
                # 保存客户端
                re.set_cookie('ticket', ticket, expires=out_time)
                # 保存服务器
                MineModel.objects.create(m_id=name.id, m_ticket=ticket, m_time=out_time)

                return re

            else:
                return HttpResponse('密码错误')
        else:
            return HttpResponse('用户不存在')


# 登出页面
def Loginout(request):
    if request.method == 'GET':
        tic = request.COOKIES.get('ticket')
        # 删除数据库的值
        MineModel.objects.filter(m_ticket=tic).delete()
        re = HttpResponseRedirect('/ind/home/')
        # 删除浏览器的值
        re.delete_cookie('ticket')

        return re


# 注册页面
def Register(request):
    if request.method == 'GET':
        return render(request, 'user/user_register.html')

    if request.method == 'POST':
        # 获取页面值
        name = request.POST.get('username')
        e = request.POST.get('email')
        pa = request.POST.get('password')
        ic = request.FILES.get('icon')
        # 保存数据库中
        MinModel.objects.create(
            usernam=name,
            email=e,
            password=pa,
            icon=ic,
        )

        return HttpResponseRedirect('/ind/log/')


# 购物车页面
def Car(request):
    if request.method == 'GET':
        if not request.user:
            return HttpResponseRedirect('/ind/log/')
        else:
            return render(request, 'cart/cart.html')


# 我的 页面
def Mine(request):
    if request.method == 'GET':
        # 传入浏览器字典——可以读写出待收货等状态
        date = {}
        # 通过中间键传入参数获取参数
        user = request.user
        # 判断是否有ticket值
        if user.id:
            # 和状态表关联
            o = user.ordermodel_set.all()
            a, b = 0, 0
            # 给状态赋值
            for i in o:
                if i.o_status == 0:
                    a += 1
                elif i.o_status == 1:
                    b += 1
            date = {
                'a': a,
                'b': b
            }

        return render(request, 'mine/mine.html', date)


def Market(request):
    if request.method == 'GET':
        return render(request, 'market/market.html')
