# -*- coding: utf-8 -*-

#  Copyright (c) 2021.  TheFox

from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Schedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='id пользователя', unique=False, help_text='Id пользователя должен быть в виде одного числа', null=True)
    time_start = models.TimeField(verbose_name='время начала', max_length=50, unique=False)
    time_end = models.TimeField(verbose_name='время конца', max_length=50, unique=False)
    date = models.DateField(verbose_name='дата', unique=False, null=True)
    affair = models.CharField(verbose_name='дело', max_length=200, unique=False, help_text='Дела должны быть в виде обычного текста', blank=False)
    note = models.CharField(verbose_name='заметка', max_length=200, unique=False, help_text='Заметки должны быть в виде обычного текста', blank=True)
    homework = models.CharField(verbose_name='домашнее задание', max_length=200, unique=False, default=None, help_text='Домашнее задание должны быть в виде обычного текста',
                                blank=True)
    is_ready = models.BooleanField(verbose_name='готово?', default=False, help_text='Готово? принимает только значение True или False')

    # def get_absolute_url(self):
    #     return reverse('Schedule:schedule', kwargs={'user_id': self.user_id})

    def __str__(self):
        return f"{self.pk}-{self.user.username}-{self.affair}"

    class Meta:
        managed = True
        verbose_name = 'расписание'
        ordering = ['date', ]
