# -*- coding: utf-8 -*-
from django.urls import path

from TimeTable.views import index

app_name = 'Schedule'
urlpatterns = [
    path('', index, name='schedule_list'),
]
