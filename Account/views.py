# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from Account.forms import RegisterAccountForm


class RegisterAccount(SuccessMessageMixin, CreateView):
    """
    Работаем с моделью User
    Используем форму RegisterAccountForm
    Html шаблон показыем registration.html
    Если регистрация успешно сделана, то выводим передаём сообщение "Вы успешно зарегистрировались"
    Если регистрация успешно сделана, то переходим по ссылке на страницу авторизации
    """
    model = User
    form_class = RegisterAccountForm
    template_name = 'Account/registration.html'
    success_message = f'Вы успешно зарегистрировались'
    success_url = reverse_lazy('Account:login')
