from django import forms
from datetime import date
from .models import CHOICES_status
from django.core.exceptions import ValidationError


def date_valid(value):
    today = date.today()
    if value < today:
        raise ValidationError('Ошибка даты')

class CreateTask(forms.Form):
    name = forms.CharField(label='Название заявки', max_length=64, required=True)
    about = forms.CharField(label='Описание заявки', widget=forms.Textarea, required=True)
    image = forms.ImageField(required=False)
    expiration_date = forms.DateField(label='Дата истечения срока заявки', validators=[date_valid], widget=forms.widgets.DateInput(attrs={'type': 'date'}), required=True)
    status = forms.ChoiceField(label='Статус', choices=CHOICES_status)


