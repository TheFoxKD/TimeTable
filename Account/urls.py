# -*- coding: utf-8 -*-
from django.urls import path

from Account.views import SignInAccount, SignUpAccount

app_name = 'Account'
urlpatterns = [
    path('sign_up/', SignUpAccount.as_view(), name='sign_up'),
    path('sign_in/', SignInAccount.as_view(), name='sign_in'),
]
