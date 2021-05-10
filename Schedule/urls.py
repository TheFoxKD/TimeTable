# -*- coding: utf-8 -*-

#  Copyright (c) 2021.  TheFox

from django.urls import path
from django.views.decorators.cache import cache_page

from Schedule.views import add_govno, DeleteAffairSchedule, DetailSchedule, UpdateAffairSchedule

app_name = 'Schedule'
urlpatterns = [
    path('<int:user_id>/', cache_page(5 * 0)(DetailSchedule.as_view()), name='schedule'),
    path('edit/<int:pk>/', UpdateAffairSchedule.as_view(), name='update_schedule'),
    path('delete/<int:pk>/', DeleteAffairSchedule.as_view(), name='delete_schedule'),
    path('', add_govno, name='main'),
    ]
