# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from smart_selects.db_fields import ChainedForeignKey


class Place(models.Model):
    name = models.CharField(max_length=150, verbose_name='городской округ / Муниципальный район', blank=False)

    def __str__(self):
        return self.name


class Locality(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='городской округ / Муниципальный район')
    name = models.CharField(max_length=150, verbose_name='населённый пункт', blank=False)

    def __str__(self):
        return f'{self.name}'


class Type_of_oo(models.Model):
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE, verbose_name='населённый пункт')
    name = models.CharField(max_length=150, verbose_name='тип ОО', blank=False)

    def __str__(self):
        return f'{self.name}'


class Educational_organization(models.Model):
    type_of_oo = models.ForeignKey(Type_of_oo, on_delete=models.CASCADE, verbose_name='тип ОО')
    name = models.CharField(max_length=150, verbose_name='образовательная организация', blank=False)

    def __str__(self):
        return f'{self.name}'


class Giseo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', blank=False)
    login = models.CharField(max_length=150, verbose_name='логин', blank=False)
    password = models.CharField(max_length=100, verbose_name='пароль', blank=False)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='городской округ / Муниципальный район')
    locality = ChainedForeignKey(Locality, chained_field='place', chained_model_field='place', auto_choose=True, sort=True, verbose_name='населённый пункт')
    type_of_oo = ChainedForeignKey(Type_of_oo, chained_field='locality', chained_model_field='locality', auto_choose=True, sort=True, verbose_name='тип ОО')
    educational_organization = ChainedForeignKey(Educational_organization, chained_field='type_of_oo', chained_model_field='type_of_oo', auto_choose=True, sort=True,
                                                 verbose_name='образовательная организация')

    def __str__(self):
        return f"{self.login} - {self.user.username}"

    class Meta:
        managed = True
        verbose_name = 'giseo'
        verbose_name_plural = "giseo's"
        ordering = ['user', 'login', 'place']
