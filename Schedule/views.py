# -*- coding: utf-8 -*-

#  Copyright (c) 2021. TheFox

# Create your views here.
import datetime

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from Account.models import Giseo
from Schedule.forms import CreateAffairScheduleForm
from Schedule.models import Schedule
from Schedule.parser import parsing


class DetailSchedule(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """
    Страница расписания для определённого пользователя с возможностью создания на ней нового дела
    model = Schedule - модель, которую использует данная страница
    template_name = Schedule/schedule.html - шаблон, который использует страница
    context_object_name = schedule - переменная, которая используеися в HTML коде (не нужна)
    form_class = CreateAffairScheduleForm - форма, которая используется на этой странице
    """
    model = Schedule
    template_name = 'Schedule/schedule.html'
    context_object_name = 'schedule'
    form_class = CreateAffairScheduleForm

    def form_valid(self, form):
        """
        Данная функция вызывается, если форма прошла валидацию. Когда данная фукнция вызывается мы подставляем в форму id пользователя, чтобы далее он записался в бд
        :param form:
        :type form:
        :return: form
        :rtype:
        """
        form.instance.user = User.objects.get(pk=self.kwargs['user_id'])
        return super(DetailSchedule, self).form_valid(form)

    def test_func(self):
        """
        Данная функция вызывается при загрузке страницы. Данная функция проверяет есть ли доступ у пользователя к данной странице. У нас два условия, чтобы пользователь получил
        доступ: 1. Если id пользователя в url строке соответсвует id пользователя, который совершает данный запрос 2. Если пользователь, который совершает  имеет статус stuff = 1
        :return: True or False
        :rtype:
        """
        if self.kwargs['user_id'] == self.request.user.id:
            return True
        elif self.request.user.is_staff:
            return True

    def get_success_url(self):
        """
        Данная функция вызывается после успешного POST запроса. Данная функция перенаправляет на пользователя на страницу с его расписанием после создания нового дела
        :return: Redirect на опр. страницу
        :rtype:
        """
        return reverse_lazy('Schedule:schedule', kwargs={'user_id': self.kwargs['user_id']})

    def get_context_data(self, *, object_list=None, **kwargs):
        """
        Данная функция вызывается после получения пользователя доступа к странице. Тут фильтруется модель под рамки начала недели и конца недели. Разбивается на каждый день
        недели и далее в HTML коде используется для получения дел для каждого дня
        :param object_list:
        :type object_list:
        :param kwargs:
        :type kwargs:
        :return: context
        :rtype:
        """
        context = super(DetailSchedule, self).get_context_data(**kwargs)

        date = datetime.date.today()
        start_week = date - datetime.timedelta(date.weekday())
        end_week = start_week + datetime.timedelta(7)
        # Для расписания
        model = Schedule.objects.filter(user=self.kwargs['user_id'], date__range=[start_week, end_week])
        context['mon'] = model.filter(date__week_day=2).order_by('time_start')
        context['tue'] = model.filter(date__week_day=3).order_by('time_start')
        context['wed'] = model.filter(date__week_day=4).order_by('time_start')
        context['thu'] = model.filter(date__week_day=5).order_by('time_start')
        context['fri'] = model.filter(date__week_day=6).order_by('time_start')
        context['sat'] = model.filter(date__week_day=7).order_by('time_start')
        context['sun'] = model.filter(date__week_day=1).order_by('time_start')
        # Для дат
        date_generated = [start_week + datetime.timedelta(days=x) for x in range(0, (end_week - start_week).days)]
        context['mon_date'] = date_generated[0]
        context['tue_date'] = date_generated[1]
        context['wed_date'] = date_generated[2]
        context['thu_date'] = date_generated[3]
        context['fri_date'] = date_generated[4]
        context['sat_date'] = date_generated[5]
        context['sun_date'] = date_generated[6]
        context['name_user'] = User.objects.get(pk=self.kwargs['user_id']).username
        return context


class UpdateAffairSchedule(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    model = Schedule - это модель, на которой построена данная страница
    template_name = Schedule/update_schedule.html - это HTML код, который вызывается при загрузке страницы
    form_class = CreateAffairScheduleForm - это форма, с которой работает данная страница
    """
    model = Schedule
    template_name = 'Schedule/update_schedule.html'
    form_class = CreateAffairScheduleForm

    def test_func(self):
        """
        Данная функция проверяет наличи доступа пользователя к данной странице.
        :return: True or False
        :rtype:
        """
        obj = Schedule.objects.get(pk=self.kwargs['pk'])
        if obj.user.id == self.request.user.id:
            return True
        elif self.request.user.is_staff:
            return True

    def get_success_url(self):
        """
        Данная функция после успешного POST запроса, перенаправляет пользователя на его расписание
        :return: Redirect на его расписание
        :rtype:
        """
        return reverse_lazy('Schedule:schedule', kwargs={'user_id': self.object.user.id})


class DeleteAffairSchedule(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    model = Schedule - это модель, на которой построена данная страница
    template_name = Schedule/delete_schedule.html - это HTML код, который вызывается при загрузке страницы
    """
    model = Schedule
    template_name = 'Schedule/delete_schedule.html'

    def get_success_url(self):
        """
        Данная функция после успешного POST запроса, перенаправляет пользователя на его расписание
        :return: Redirect на его расписание
        :rtype:
        """
        return reverse_lazy('Schedule:schedule', kwargs={'user_id': self.object.user.id})

    def test_func(self):
        """
        Данная функция проверяет наличи доступа пользователя к данной странице.
        :return: True or False
        :rtype:
        """
        obj = Schedule.objects.get(pk=self.kwargs['pk'])
        if obj.user.id == self.request.user.id:
            return True
        elif self.request.user.is_staff:
            return True


def test(request):
    giseo_obj = Giseo.objects.get(user=)
    objects = parsing(giseo_obj.place.name, giseo_obj.locality.name, giseo_obj.type_of_oo.name, giseo_obj.educational_organization.name, giseo_obj.login, giseo_obj.password)
    print(objects)
    # Schedule.objects.bulk_create(sch)
    return HttpResponse('Всё ок)')
