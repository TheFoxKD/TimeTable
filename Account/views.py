#  Copyright (c) 2021. TheFox

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
    model = User - это модель, с которой работает данная страница
    form_class = SignUpAccountForm -это форма, с которой работает данная страница
    template_name = Account/sign_up.html - это HTML код, который вызывается при загрузке данной страницы
    success_message = Вы успешно прошли регистрацию - это текст сообщения, которое передаётся в message с указателем success
    """
    model = User
    form_class = SignUpAccountForm
    template_name = 'Account/sign_up.html'
    success_message = f'Вы успешно прошли регистрацию'

    def get_success_url(self):
        """
        Данная функция после успешного заполнения формы перенаправляет на страницу авторизации
        :return: Redirect на страницу авторизации
        :rtype:
        """
        return reverse_lazy('Account:sign_in')


class SignInAccount(SuccessMessageMixin, LoginView):
    """
    form_class = SignInAccountForm - это форма, с которой работает данная страница
    template_name = Account/sign_in.html - это HTML код, который вызывается при загрузке данной страницы
    success_message = Вы успешно вошли в свой аккаунт - это текст сообщения, которое передаётся в message с указателем success
    """
    form_class = SignInAccountForm
    template_name = 'Account/sign_in.html'
    success_message = f'Вы успешно вошли в свой аккаунт'

    def get_success_url(self):
        """
        Данная функция после успешного заполнения формы перенаправляет на страницу расаписания пользователя, который совершает запрос
        :return: Redirect на страницу расписания
        :rtype:
        """
        return reverse_lazy('Schedule:schedule', kwargs={'user_id': self.request.user.id})


class SignInGiseo(LoginRequiredMixin, SuccessMessageMixin, FormView):
    """
    model = Giseo - это модель, с которой работает данная страница
    form_class = SignInGiseoForm - это форма, с которой работает данная странциа
    template_name = Account/sign_in_giseo.html - это HTML код, который вызывается при загрузке данной страницы
    success_message = Вы успешно подключили giseo к своему аккаунту - это текст сообщения, которое передаётся в message с указателем success
    """
    model = Giseo
    form_class = SignInGiseoForm
    template_name = 'Account/sign_in_giseo.html'
    success_message = f'Вы успешно подключили giseo к своему аккаунту'

    def get_success_url(self):
        """
        Данная функция после успешного заполнения формы перенаправляет на страницу расаписания пользователя, который совершает запрос
        :return: Redirect на страницу расписания
        :rtype:
        """
        return reverse_lazy('Schedule:schedule', kwargs={'user_id': self.request.user.id})

    def form_valid(self, form):
        """
        Данная функция выполняется, если форма прошла валидацию. Данная функция совершает попытку получить объект с user = пользователю, который совершает данный запрос. Если
        объект с данным пользователем найден, то мы обновляем поля в данного объекта, а не создаём новую запись в бд. Если ошибка, то мы создаём новую запись с данными из формы
        :param form:
        :type form:
        :return: form
        :rtype:
        """
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
                                 locality=form.instance.locality, type_of_oo=form.instance.type_of_oo, educational_organization=form.instance.educational_organization)

        return super(SignInGiseo, self).form_valid(form)
