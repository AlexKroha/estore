from shop.models import Category


def get_category(request):
    categories = Category.objects.all().order_by()
    return locals()