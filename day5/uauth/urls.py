from django.conf.urls import url
from uauth import views

urlpatterns = [
    url(r'^re/', views.regist),
    url(r'^lo/', views.login),
    url(r'^out/', views.logout),
    url(r'djlo/', views.djlogin),
    url(r'djre/', views.djregist),
    url(r'djout/', views.djout),
]
