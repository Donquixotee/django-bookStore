from django.db import reset_queries
from django.shortcuts import get_object_or_404, render

from .models import Category, Product




def products_all(request):
    products = Product.products.all()
    
    return render(request, 'store/home.html', {'products': products})

def count_objects(request):
    count= Product.objects.all().count()
    print(count)
    context= {
        'count': count
    }
    return render(request, 'store/home.html',context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/single.html', {'product': product})

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})