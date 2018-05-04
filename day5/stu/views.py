from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.urls import reverse

from stu.models import Student, StudentInfo
from stu.serializers import StudentSerializer
from uauth.models import Users
import logging

from rest_framework import mixins, viewsets

logger = logging.getLogger('stu')


def index(requset):
    if requset.method == 'GET':
        # # 获取cookie的值中的ticket值
        # t = requset.COOKIES.get('ticket')
        # if not t:
        #     return HttpResponseRedirect('/uau/lo/')
        # if Users.objects.filter(u_ticket=t).exists():
        #     #获取所有信息
        #     stuinfo = StudentInfo.objects.all()
        #     return render(requset, 'index.html',{'stuinfo':stuinfo})
        # else:
        #     return HttpResponseRedirect('/uau/lo/')

        stuinfo = StudentInfo.objects.all()
        logger.info('url:%s method:%s 获取学生信息成功' % (requset.path, requset.method))
        return render(requset, 'index.html', {'stuinfo': stuinfo})


def addStu(request):
    if request.method == 'GET':
        return render(request, 'add.html')

    if request.method == 'POST':
        # 跳转详情
        name = request.POST.get('name')
        tel = request.POST.get('tel')

        stu = Student.objects.create(
            s_name=name,
            s_tel=tel
        )
        # 传递参数 kwargs位置
        return HttpResponseRedirect(
            reverse('s:addin', kwargs={'stu': stu.id})
        )


def addStuInfo(request, stu):
    if request.method == 'GET':
        # 获取
        return render(request, 'addStu.html')

    if request.method == 'POST':
        # stu_id = request.POST.get('stu')
        addr = request.POST.get('addr')
        # 添加头像
        img = request.FILES.get('img')

        StudentInfo.objects.create(i_addr=addr, s_id=stu, i_image=img)
        # 不加reverse
        return HttpResponseRedirect(
            '/st/index/'
        )


def stuPage(request):
    if request.method == 'GET':
        # 获取参数如果为空就是1 表示首页
        pag = int(request.GET.get('page_id', 1))
        stu = StudentInfo.objects.all()
        pagina = Paginator(stu, 3)
        pagee = pagina.page(pag)

        return render(request, 'index_page.html', {'stu': pagee})


class Aba(mixins.ListModelMixin,
          mixins.RetrieveModelMixin,
          mixins.UpdateModelMixin,
          mixins.DestroyModelMixin,
          mixins.CreateModelMixin,
          viewsets.GenericViewSet):
    # 查询所有信息
    queryset = Student.objects.all()
    # 序列化
    serializer_class = StudentSerializer