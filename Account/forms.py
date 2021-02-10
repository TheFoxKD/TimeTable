# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from Account.models import Giseo

place_right = (
    'Городской округ Воркута', 'Городской округ Вуктыл', 'Городской округ Инта', 'Городской округ Печора', 'Городской округ Сосногорск', 'Городской округ Сыктывкар',
    'Городской округ Усинск', 'Городской округ Ухта', 'Ижемский район', 'Княжпогостский район', 'Койгородский район', 'Корткеросский район', 'Прилузский район',
    'Сыктывдинский район', 'Сысольский район', 'Троицко-Печорский район', 'Удорский район', 'Усть-Вымский район', 'Усть-Куломский район', 'Усть-Цилемский район')
locality_right = (
    'Воркута, г.', 'Вуктыл, г.', 'Инта, г.', 'Печора, г.', 'Сосногорск, г.', 'Сыктывкар, г.', 'Усинск, г.', 'Ухта, г.', 'Бакур, д.', 'Большое Галово, д.', 'Брыкаланск, с.',
    'Варыш, д.', 'Вертеп, д.', 'Гам, д.', 'Диюр, д.', 'Ижма, с.', 'Кельчиюр, с.', 'Кипиево, с.', 'Койю, п.', 'Краснобор, с.', 'Ласта, д.', 'Мохча, с.', 'Мошъюга, д.',
    'Няшабож, с.', 'Сизябск, с.', 'Том, п.', 'Усть-Ижма, д.', 'Щельяюр, п.', 'Емва, г.', 'Серёгово, с.', 'Синдор, пгт.', 'Тракт, п.', 'Чернореченский, п.', 'Чиньяворык, п.',
    'Шошка, с.', 'Вежъю, п.', 'Грива, с.', 'Зимовка, п.', 'Кажым, п.', 'Койгородок, с.', 'Койдин, п.', 'Кузьёль, п.', 'Подзь, п.', 'Аджером, п.', 'Богородск, с.',
    'Большелуг, с.', 'Визябож, п.', 'Выльыб, д.', 'Керес, с.', 'Корткерос, с.', 'Мордино, с.', 'Намск, п.', 'Нёбдино, с.', 'Нившера, с.', 'Подтыбок, п.', 'Подъельск, с.',
    'Приозёрный, п.', 'Сторожевск, с.', 'Троицк, д.', 'Усть-Лэкчим, п.', 'Вухтым, п.', 'Гурьевка, с.', 'Летка, с.', 'Лойма, с.', 'Мутница, с.', 'Ношуль, с.', 'Объячево, с.',
    'Спаспоруб, с.', 'Черёмуховка, с.', 'Читаево, с.', 'Якуньёль, п.', 'Выльгорт, с.', 'Зеленец, с.', 'Лэзым, с.', 'Нювчим, п.', 'Пажга, с.', 'Палевицы, с.', 'Слудка, с.',
    'Часово, с.', 'Шошка, с.', 'Ыб, с.', 'Яснэг, п.', 'Визинга, с.', 'Визиндор, п.', 'Горьковская, д.', 'Заозерье, п.', 'Куратово, с.', 'Межадор, с.', 'Первомайский, п.',
    'Пыёлдино, с.', 'Чухлэм, с.', 'Белый Бор, п.', 'Комсомольск-на-Печоре, п.', 'Митрофан-Дикост, п.', 'Мылва, п.', 'Нижняя Омра, п.', 'Приуральский, п.', 'Русаново, п.',
    'Троицко-Печорск, пгт.', 'Усть-Илыч, с.', 'Якша, п.', 'Благоево, пгт.', 'Большая Пучкома, с.', 'Большая Пысса, с.', 'Буткан, с.', 'Важгорт, с.', 'Вожский, п.',
    'Глотово, с.', 'Ёдва, п.', 'Ёртом, с.', 'Кослан, с.', 'Междуреченск, пгт.', 'Мозындор, п.', 'Солнечный, п.', 'Усогорск, пгт.', 'Чернутьево, с.', 'Чим, п.', 'Чупрово, с.',
    'Айкино, с.', 'Вежайка, п.', 'Гам, с.', 'Донаёль, п.', 'Жешарт, пгт.', 'Илья-Шор, п.', 'Казлук, п.', 'Кожмудор, с.', 'Мадмас, п.', 'Микунь, г.', 'Студенец, п.',
    'Усть-Вымь, с.', 'Бадьёльск, д.', 'Верхний Воч, д.', 'Вольдино, с.', 'Деревянск, с.', 'Диасёръя, п.', 'Дон, с.', 'Зимстан, п.', 'Кебанъёль, п.', 'Керчомъя, с.',
    'Лопъювад, п.', 'Мыёлдино, с.', 'Нижний Воч, с.', 'Носим, с.', 'Озъяг, п.', 'Пожег, с.', 'Пожегдин, д.', 'Помоздино, с.', 'Пузла, д.', 'Руч, с.', 'Скородум, д.',
    'Смолянка, п.', 'Тимшер, п.', 'Усть-Кулом, с.', 'Усть-Нем, с.', 'Шэръяг, п.', 'Югыдъяг, п.', 'Ягкедж, п.', 'Ярашъю, п.', 'Ёрмица, с.', 'Замежная, с.', 'Коровий Ручей, с.',
    'Медвежка, п.', 'Нерица, с.', 'Новый Бор, п.', 'Окунев Нос, с.', 'Синегорье, п.', 'Среднее Бугаево, с.', 'Степановская, д.', 'Трусово, с.', 'Усть-Цильма, с.',
    'Филиппово, д.', 'Хабариха, с.', 'Чукчино, д.')

type_of_oo_right = ('Дошкольное образование', 'Общеобразовательная', 'Дополнительное образование детей')


class SignUpAccountForm(UserCreationForm):
    """Переделываем стандартную регистрацию из django, добавляя к ней поля ввода mail. Присваем ко всем полям class от bs"""
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин'}), max_length=100, label='Логин')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Эл. почтовый ящик'}), max_length=64, label='Эл. почтовый ящик')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}), max_length=50, label='Пароль')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}), max_length=50, label='Подтверждение пароля')

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)


class SignInAccountForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин'}), max_length=100, label='Логин пользователя')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}), max_length=50, label='Пароль')


class SignInGiseoForm(forms.ModelForm):
    login = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин'}), max_length=150, label='Логин')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}), max_length=100, label='Пароль')
    place = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Городской округ / Муниципальный район'}), max_length=150,
                            label='Городской округ / Муниципальный район')
    locality = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Населённый пункт'}), max_length=150, label='Населённый пункт')
    type_of_oo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Тип ОО'}), max_length=150, label='Тип ОО')
    educational_organization = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Образовательная организация'}), max_length=150,
                                               label='Образовательная организация')

    class Meta:
        model = Giseo
        fields = ('login', 'password', 'place', 'locality', 'type_of_oo', 'educational_organization')

    def clean_place(self):
        place_data = self.cleaned_data['place']
        if not place_data in place_right:
            raise ValidationError('Данного городского округа или муниципального района не существует')
        return place_data

    def clean_locality(self):
        locality_data = self.cleaned_data['locality']
        if not locality_data in locality_right:
            raise ValidationError('Данного населённого пункта не существует')
        return locality_data
