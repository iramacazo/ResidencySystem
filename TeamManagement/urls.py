from . import views
from django.conf.urls import url

urlpatterns = [

    url(r'^$', views.index, name='index'),

    url(r'^ajax/validateteamname$', views.validateteamname, name='validateteamname'),

    url(r'^delete/(?P<groupid>\d+)/', views.deleteteam, name='deleteteam')
]
