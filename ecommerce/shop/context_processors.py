from shop.models import Category
def menu_link(request):
    c=Category.objects.all()
    return {'link':c}