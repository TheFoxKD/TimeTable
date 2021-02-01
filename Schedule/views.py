from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView

from Schedule.models import Schedule


class DetailNote(DetailView):
    model = Schedule
    template_name = 'Schedule/main.html'
    context_object_name = 'schedule'
