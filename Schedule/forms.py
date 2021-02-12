# -*- coding: utf-8 -*-
from django import forms

from Schedule.models import Schedule


class CreateAffairScheduleForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Дата', 'type': 'date'}), label='Дата')
    affair = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Дело|Предмет'}), label='Дело|Предмет')
    time = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Время начала и окончания дела'}), label='Время начала и оканчания дела',
                           help_text='Должно быть записано в формате hh:mm-hh:mm')
    homework = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Домашнее задание'}), label='Домашнее задание', required=False)
    note = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Заметка'}), label='Заметка', required=False)
    is_ready = forms.NullBooleanField(widget=forms.NullBooleanSelect(attrs={'class': 'form-control'}), label='Готово?')

    class Meta:
        model = Schedule
        fields = ('date', 'affair', 'time', 'homework', 'note', 'is_ready')
