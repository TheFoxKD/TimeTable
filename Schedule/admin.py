from django.contrib import admin

# Register your models here.
from Schedule.models import Schedule


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    fields = ('user', 'time_start', 'time_end', 'date', 'affair', 'note', 'homework', 'is_ready')
    list_display = ('user', 'time_start', 'time_end', 'date', 'affair', 'note', 'homework', 'is_ready')
    list_display_links = ('user', 'time_start', 'time_end', 'date', 'affair', 'note', 'homework', 'is_ready')
    list_filter = ('user',)
