from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'city', 'address']

        labels = {
            'first_name': 'Ваше имя',
            'last_name': 'Ваша фамилия',
            'phone_number': 'Номер телефона',
            'email': 'Электронная почта',
            'city': 'Город',
            'address': 'Улица, дом, кв',
        }
        help_texts = {
            'first_name': '<p class="text-primary m-0" style="font-family: Bitstream Vera Sans Mono;font-size: 15px;">Обязательное поле</p>',
            'last_name': '<p class="text-primary m-0" style="font-family: Bitstream Vera Sans Mono;font-size: 15px;">Обязательное поле</p>',
            'phone_number': '<p class="text-primary m-0" style="font-family: Bitstream Vera Sans Mono;font-size: 15px;">В формате 8-999-999-99-99</p>',
            'city': '<p class="text-primary m-0" style="font-family: Bitstream Vera Sans Mono;font-size: 15px;">Обязательное поле</p>',
            'address': '<p class="text-primary m-0" style="font-family: Bitstream Vera Sans Mono;font-size: 15px;">Обязательное поле</p>',
            'email': '<p class="text-primary m-0" style="font-family: Bitstream Vera Sans Mono;font-size: 15px;">Для улучшения сервиса</p>',
        }