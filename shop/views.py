from django.shortcuts import render, get_object_or_404

from cart.forms import CartAddProductForm

from .models import Category, Product
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from sendemail.forms import ContactForm
from estore.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL


# Create your views here.


def home(request):
    template = 'shop/index.html'
    products = Product.objects.filter(available=True)

    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        # если метод POST, проверим форму и отправим письмо
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(f'{subject} от {from_email}', message,
                          DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            return redirect('success')
    else:
        return HttpResponse('Неверный запрос.')
    context = {
        'products': products,
        'form': form,
    }
    return render(request, template, context)


def category_list(request, category_slug=None):
    return render(request, 'shop/category_list.html', {
    })


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all().order_by()
    products = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product_list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug
                                )
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }

    return render(request, 'shop/product_detail.html', context)
