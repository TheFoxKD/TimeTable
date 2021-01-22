# -*- coding: utf-8 -*-
from django.urls import path

from Account.views import RegisterAccount

app_name = 'Account'
urlpatterns = [
    path('sign_up', RegisterAccount.as_view(), name='register'),
    path('sign_up', RegisterAccount.as_view(), name='login'),
]
