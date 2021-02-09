# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Schedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='id пользователя', unique=False, help_text='Id пользователя должен быть в виде одного числа')
    time = models.CharField(verbose_name='время', max_length=100, unique=False, help_text='Время в формате h:m-h:m')
    date = models.DateField(verbose_name='дата', unique=False, help_text='Дата в формате YYYY-MM-DD')
    affair = models.CharField(verbose_name='дело', max_length=200, unique=False, help_text='Дела должны быть в виде обычного текста')
    note = models.CharField(verbose_name='заметка', max_length=200, unique=False, help_text='Заметки должны быть в виде обычного текста')
    homework = models.CharField(verbose_name='домашнее задание', max_length=200, unique=False, default=None, help_text='Домашнее задание должны быть в виде обычного текста')
    is_ready = models.BooleanField(verbose_name='готово?', default=False, help_text='Готово? принимает только значение True или False')

    def __str__(self):
        return f"{self.user.username} - это его расписание"

    class Meta:
        managed = True
        verbose_name = 'расписание'
        verbose_name_plural = 'расписании'
        ordering = ['date', ]
