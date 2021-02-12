# -*- coding: utf-8 -*-
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

import Account
from Account.forms import SignInAccountForm, SignInGiseoForm, SignUpAccountForm
# Create your views here.
from Account.models import Giseo


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


class SignInGiseo(LoginRequiredMixin, SuccessMessageMixin, FormView):
    model = Giseo
    form_class = SignInGiseoForm
    template_name = 'Account/sign_in_giseo.html'
    success_message = f'Вы успешно подключили giseo к своему аккаунту'
    success_url = reverse_lazy('main_page')

    def form_valid(self, form):
        try:
            post = Giseo.objects.get(user=self.request.user)
            post.login = form.instance.login
            post.password = make_password(form.instance.password)
            post.place = form.instance.place
            post.locality = form.instance.locality
            post.type_of_oo = form.instance.type_of_oo
            post.educational_organization = form.instance.educational_organization
            post.save()
        except Account.models.Giseo.DoesNotExist:
            Giseo.objects.create(user=self.request.user, login=form.instance.login, password=make_password(form.instance.password), place=form.instance.place,
                                 locality=form.instance.locality, type_of_oo=form.instance.type_of_oo,
                                 educational_organization=form.instance.educational_organization)

        return super(SignInGiseo, self).form_valid(form)
