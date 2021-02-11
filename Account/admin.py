# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from Account.models import Educational_organization, Giseo, Locality, Place, Type_of_oo


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    fields = ('name',)


@admin.register(Locality)
class LocalityAdmin(admin.ModelAdmin):
    list_display = ('place', 'name')
    list_display_links = ('place', 'name')
    fields = ('place', 'name')
    save_as = True
    save_on_top = True

@admin.register(Type_of_oo)
class Type_of_ooAdmin(admin.ModelAdmin):
    fields = ('locality', 'name')


@admin.register(Educational_organization)
class Educational_organizationAdmin(admin.ModelAdmin):
    fields = ('type_of_oo', 'name')


@admin.register(Giseo)
class GiseoAdmin(admin.ModelAdmin):
    fields = ('user', 'login', 'password', 'place', 'locality', 'type_of_oo', 'educational_organization')
