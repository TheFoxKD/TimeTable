# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Giseo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', blank=False)
    login = models.CharField(max_length=150, verbose_name='логин', blank=False)
    password = models.CharField(max_length=100, verbose_name='пароль', blank=False)
    place = models.CharField(max_length=150, verbose_name='городской округ / Муниципальный район', blank=False)
    locality = models.CharField(max_length=150, verbose_name='населённый пункт', blank=False)
    type_of_oo = models.CharField(max_length=150, verbose_name='тип ОО', blank=False)
    educational_organization = models.CharField(max_length=150, verbose_name='образовательная организация', blank=False)

    def __str__(self):
        return f"{self.login} - {self.user.username}"

    class Meta:
        managed = True
        verbose_name = 'giseo'
        verbose_name_plural = "giseo's"
        ordering = ['user', 'login', 'place']
