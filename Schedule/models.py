# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Schedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='пользователь')
    note = models.ForeignKey('Note', on_delete=models.PROTECT, verbose_name='заметка')


class Note(models.Model):
    class DayWeak(models.TextChoices):
        MON = ('Пн', 'Понедельник')
        TUE = ('Вт', 'Вторник')
        WEN = ('Ср', 'Среда')
        THUR = ('Чт', 'Четверг')
        FRI = ('Пт', 'Пятница')
        SAT = ('Сб', 'Суббота')
        SUN = ('Вс', 'Воскресенье')

    content = models.TextField(verbose_name='контент')
    date_add = models.DateTimeField(verbose_name='дата добавления', auto_now_add=True)
    dead_line = models.DateTimeField(verbose_name='дед лайн')
    day_on_weak = models.CharField(choices=DayWeak.choices, verbose_name='день недели', max_length=2)
