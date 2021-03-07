# -*- coding: utf-8 -*-

#  Copyright (c) 2021. TheFox

from django.shortcuts import render
from loguru import logger


@logger.catch
def index(request):
    return render(request, template_name='TimeTable/index.html')
