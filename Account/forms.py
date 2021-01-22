# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterAccountForm(UserCreationForm):
    """Переделываем стандартную регистрацию из django, добавляя к ней поля ввода mail. Присваем ко всем полям class от bs"""
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин'}), max_length=100, label='Логин')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Эл. почтовый ящик'}), max_length=64, label='Эл. почтовый ящик')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}), max_length=50, label='Пароль')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}), max_length=50, label='Подтверждение пароля')

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)
