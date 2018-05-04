from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from stu import views

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'student', views.Aba)

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^add/', login_required(views.addStu), name='add'),
    url(r'^addinf/(?P<stu>\d+)', views.addStuInfo, name='addin'),
    url(r'^pag/', views.stuPage)

]

urlpatterns += router.urls
