from . import views
from django.conf.urls import url

urlpatterns = [

    url(r'^$', views.index),

    url(r'^ajax/validateteamname$', views.validateteamname, name='validateteamname')
]
