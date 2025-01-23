from django.forms import ModelForm, TextInput, NumberInput, Select
from .models import Chek


class ChekForm(ModelForm):
    class Meta:
        model = Chek
        fields = '__all__'

        widgets = {
            'status': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Выберите статус'
            }),
            'type': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Выберите тип'
            }),
            'category': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Выберите категорию'
            }),
            'sub_categoty': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Выберите подкатегорию'
            }),
            "summ": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Сумма'
            }),
            "coment": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Коментарий'
            }),
        }
