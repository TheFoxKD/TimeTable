# -*- coding: utf-8 -*-

#  Copyright (c) 2021. TheFox

from django.urls import path

from Schedule.views import DetailSchedule, test, UpdateAffairSchedule

app_name = 'Schedule'
urlpatterns = [
    path('<int:user_id>/', DetailSchedule.as_view(), name='schedule'),
    path('<int:user_id>/<int:pk>/', UpdateAffairSchedule.as_view(), name='update_schedule'),
    path('', test, name='test'),
]
