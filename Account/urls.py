# -*- coding: utf-8 -*-

#  Copyright (c) 2021. TheFox

from django.urls import path

from Account.views import LogOutAccount, SignInAccount, SignInGiseo, SignUpAccount

app_name = 'Account'
urlpatterns = [
    path('sign_up/', SignUpAccount.as_view(), name='sign_up'),
    path('sign_in/', SignInAccount.as_view(), name='sign_in'),
    path('sign_in_giseo/', SignInGiseo.as_view(), name='sign_in_giseo'),
    path('logout/', LogOutAccount.as_view(), name='logout'),
]
