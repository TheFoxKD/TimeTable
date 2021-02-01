from django.contrib import admin

# Register your models here.
from Schedule.models import Note, Schedule


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['id', 'note_id', 'user_id']


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'date_add', 'dead_line', 'day_on_weak']
