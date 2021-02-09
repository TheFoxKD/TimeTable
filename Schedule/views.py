# Create your views here.
from django.views.generic import DetailView

from Schedule.models import Schedule


class DetailSchedule(DetailView):
    model = Schedule
    template_name = 'Schedule/schedule.html'
    context_object_name = 'schedule'

    def get_queryset(self):
        model = Schedule.objects.filter(user=self.kwargs['pk'])
        return model
