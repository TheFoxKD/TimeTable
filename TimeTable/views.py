# -*- coding: utf-8 -*-
from django.shortcuts import render


def index(request):
    return render(request, template_name='TimeTable/index.html')
