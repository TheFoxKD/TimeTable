# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from Account.forms import SignInAccountForm, SignUpAccountForm


# Create your views here.
class SignUpAccount(SuccessMessageMixin, CreateView):
    """
    Работаем с моделью User
    Используем форму SignUpAccountForm
    Html шаблон показыем sign_up.html
    Если регистрация успешно сделана, то выводим передаём сообщение "Вы успешно зарегистрировались"
    Если регистрация успешно сделана, то переходим по ссылке на страницу авторизации
    """
    model = User
    form_class = SignUpAccountForm
    template_name = 'Account/sign_up.html'
    success_message = f'Вы успешно прошли регистрацию'
    success_url = reverse_lazy('Account:sign_in')


class SignInAccount(SuccessMessageMixin, LoginView):
    """
    Используем форму SignInAccountForm
    Html шаблон показыем sign_in.html
    Если регистрация успешно сделана, то выводим передаём сообщение "Вы успешно вошли в свой аккаунт"
    Если авторизация успешно пройдена, то переходим по ссылке на страницу авторизации
    """
    form_class = SignInAccountForm
    template_name = 'Account/sign_in.html'
    success_message = f'Вы успешно вошли в свой аккаунт'
    success_url = reverse_lazy('Account:sign_in')
