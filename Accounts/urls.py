from . import views
from django.conf.urls import url
from django.contrib.auth.views import logout
from django.conf import settings

urlpatterns = [

    url(r'^register/', views.register, name='register'),

    url(r'^login/', views.login_view, name='login'),

    url(r'^logout/', logout, {'next_page': settings.LOGIN_REDIRECT_URL}),

    url(r'^delete/(?P<userid>\d+)/', views.deleteuser, name='deleteteam')
]
