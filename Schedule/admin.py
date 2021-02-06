from django.contrib import admin

# Register your models here.
from Schedule.models import Schedule


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    fields = ('user_id', 'time', 'date', 'affair', 'note', 'homework', 'is_ready')
