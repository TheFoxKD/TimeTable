# -*- coding: utf-8 -*-
from django.urls import path

from Schedule.views import DetailSchedule

app_name = 'Schedule'
urlpatterns = [
    path('<int:user_id>/', DetailSchedule.as_view(), name='schedule'),
]
