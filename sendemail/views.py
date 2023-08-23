from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from estore.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL


def success_view(request):
    templates = 'sendemail/send_success.html'
    return render(request, templates, context={})