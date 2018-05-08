from django.conf.urls import url
from Ind import views


urlpatterns = [
    url(r'^home/', views.Home),
    url(r'^log/', views.Login),
    url(r'^logout', views.Loginout),
    url(r'^reg/', views.Register),
    url(r'^car/', views.Car),
    url(r'^mine/', views.Mine),
    url(r'^market/', views.Market),
]


