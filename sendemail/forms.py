
# sendemail/forms.py
from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(label='Электронная почта', required=False)
    phone = forms.CharField(label='Телефон', required=True)
    subject = forms.CharField(label='Тема', required=True)
    message = forms.CharField(label='Сообщение', widget=forms.Textarea, required=True)