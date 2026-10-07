from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def home(request):
    """Home page: available products + categories with product counts."""
    products = Product.objects.filter(is_available=True).order_by('-created_date')
    product_count = products.count()
    shop_categories = Category.objects.annotate(pcount=Count('product')).order_by('category_name')
    context = {
        'products': products,
        'product_count': product_count,
        'shop_categories': shop_categories,
    }
    return render(request, 'home.html', context)


def store(request, category_slug=None):
    """Store page: all products or filtered by category slug, search (q) and sort."""
    categories = None
    products = Product.objects.filter(is_available=True)

    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=categories)

    query = request.GET.get('q', '').strip()
    if query:
        products = products.filter(product_name__icontains=query)

    sort = request.GET.get('sort', '')
    if sort == 'price_asc':
        products = products.order_by('price')
    elif sort == 'price_desc':
        products = products.order_by('-price')
    else:
        products = products.order_by('-created_date')

    product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count,
        'categories': categories,
        'query': query,
        'sort': sort,
    }
    return render(request, 'store/store.html', context)


def signin(request):
    """Sign in page (static demo)."""
    return render(request, 'signin.html')


def register(request):
    """Register page (static demo)."""
    return render(request, 'register.html')
