# -*- coding: utf-8 -*-
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from Schedule.models import Schedule


class DetailSchedule(LoginRequiredMixin, DetailView):
    model = Schedule
    template_name = 'Schedule/schedule.html'
    context_object_name = 'schedule'

    def get_queryset(self):
        return Schedule.objects.filter(user=self.request.user)
