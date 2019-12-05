# -*- coding:utf-8 -*-
__author__ = '朱永刚'

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world !  django ~~")