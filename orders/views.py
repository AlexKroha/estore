from django.core.mail import EmailMessage, send_mail, message
from django.shortcuts import render, redirect

from estore import settings
from estore.settings import EMAIL_HOST_USER, RECIPIENTS_EMAIL
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)

    if cart:
        if request.method == 'POST':
            form = OrderCreateForm(request.POST)
            if form.is_valid():
                order = form.save()
                letter_body = ('Заказ №' + str(order.id))
                letter_body += ('\nТелефон: ' + str(order.phone_number))
                letter_body += ('\nФамилия: ' + str(order.last_name))
                letter_body += ('\nАдрес: ' + str(order.city) + ', ' + str(order.address))

                for item in cart:
                    OrderItem.objects.create(order=order,
                                             product=item['product'],
                                             price=item['price'],
                                             quantity=item['quantity'])
                    letter_body += (
                            '\nТовар ' + str(item['product']) +
                            ' (' + str(item['product'].category) + ')' + ', цена за штуку - ' + str(item['price']) +
                            ', количество - ' + str(item['quantity']) + 'шт' + ', стоимость - ' + str(item['total_price'])
                                        )
                letter_body += '\nИтого - ' + str(cart.get_total_price())
                send_mail('Заказ', letter_body, settings.EMAIL_HOST_USER, RECIPIENTS_EMAIL)

                # email_body = "заказ№"  + " на сумму: "  + "руб. Детали: "
                # email = EmailMessage('Subject', email_body, EMAIL_HOST_USER, to=['sash2005-2@yandex.ru'])
                # email.send()
                # очистка корзины
                cart.clear()
                return render(request, 'orders/order_created.html',
                              {'order': order})
        else:
            form = OrderCreateForm
        return render(request, 'orders/order_create.html',
                      {'cart': cart, 'form': form})

    else:
        return redirect('category_list')