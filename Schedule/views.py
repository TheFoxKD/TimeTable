# -*- coding: utf-8 -*-
# Create your views here.
import datetime

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.views.generic import CreateView, ListView

from Account.models import Type_of_oo
from Schedule.forms import CreateAffairScheduleForm
from Schedule.models import Schedule


class DetailSchedule(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Schedule
    template_name = 'Schedule/schedule.html'
    context_object_name = 'schedule'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DetailSchedule, self).get_context_data(**kwargs)
        date = datetime.date.today()
        start_week = date - datetime.timedelta(date.weekday())
        end_week = start_week + datetime.timedelta(7)
        context['mon'] = Schedule.objects.filter(user=self.kwargs['user_id'], date__range=[start_week, end_week], date__week_day=2)
        context['tue'] = Schedule.objects.filter(user=self.kwargs['user_id'], date__range=[start_week, end_week], date__week_day=3)
        context['wed'] = Schedule.objects.filter(user=self.kwargs['user_id'], date__range=[start_week, end_week], date__week_day=4)
        context['thu'] = Schedule.objects.filter(user=self.kwargs['user_id'], date__range=[start_week, end_week], date__week_day=5)
        context['fri'] = Schedule.objects.filter(user=self.kwargs['user_id'], date__range=[start_week, end_week], date__week_day=6)
        context['sat'] = Schedule.objects.filter(user=self.kwargs['user_id'], date__range=[start_week, end_week], date__week_day=7)
        context['sun'] = Schedule.objects.filter(user=self.kwargs['user_id'], date__range=[start_week, end_week], date__week_day=1)
        return context

    def test_func(self):
        model = Schedule.objects.filter(user=self.kwargs['user_id']).first()
        if model.user.id == self.request.user.id:
            return model.user.id == self.request.user.id
        elif self.request.user.is_staff:
            return Schedule.objects.filter(user=self.kwargs['user_id'])


class CreateAffairSchedule(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Schedule
    template_name = 'Schedule/create_affair.html'
    form_class = CreateAffairScheduleForm

    def test_func(self):
        obj = self.get_object()
        if obj.user.id == self.request.user.id:
            return obj.user.id == self.request.user.id
        elif self.request.user.is_staff:
            return obj.user.id


def test(request):
    local = 177
    sch = [Type_of_oo
           (locality_id=local,
            name='Дошкольное образование'
            ),
           ]
    Type_of_oo.objects.bulk_create(sch)
    return HttpResponse('Всё ок)')
