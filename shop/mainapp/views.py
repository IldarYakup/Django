from django.shortcuts import render
from mainapp.models import Product
from django.shortcuts import get_object_or_404

# Create your views here.
#from shop.mainapp.models import ProductCategory


def main(request):
    title = 'Главная'
    products = Product.objects.all()
    content = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html', content)


def products(request):
    products = Product.objects.all()
    content = {'products': products}
    return render(request, 'mainapp/products_list.html', content)

def product(request, pk):
    product = Product.objects.filter(pk=pk)
    content = {'products': product}
    return render(request, 'mainapp/product_page.html', content)

def contact(request):
    return render(request, 'mainapp/contact.html')

