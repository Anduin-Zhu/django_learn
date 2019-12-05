# -*- coding:utf-8 -*-
__author__ = '朱永刚'

from django.urls import path,re_path
from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    path('',views.index,name = 'index'),
    path('hello/',views.hello,name='hello'),
    path('orm/',views.orm,name='orm'),

]