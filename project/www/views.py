from django.shortcuts import render,redirect
from .models import Category,Product,Cheapest
from .forms import CategoryForm,ProductForm

def index(request):
  
    return render(request, 'www/index.html', {})

def products(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductForm()
    
    products = Product.objects.all()
    return render(request, 'www/products.html', {'form': form, 'products': products})

def products_list(request):

    products = Product.objects.all()
    return render(request, 'www/products_list.html', {'products': products})







def categories(request):
    if request.method == 'POST':
            form = CategoryForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('categories')
    else:
        form = CategoryForm()
        
        categories = Category.objects.all()
        return render(request, 'www/categories.html', {'form': form, 'categories': categories})


def category_detail(request, category_id):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'www/category_detail.html', {'category': category, 'products': products})



def update_cheapest():
    cheapest_products = Product.objects.order_by('price')[:3]
    Cheapest.objects.all().delete()  # Usuń poprzednie dane z modelu Cheapest
    for product in cheapest_products:
        Cheapest.objects.create(product=product)

def cheapest(request):
    # Aktualizacja najtańszych produktów
    update_cheapest()
    # Pobranie aktualnych najtańszych produktów
    cheapest_products = Cheapest.objects.all()
    return render(request, 'www/cheapest.html', {'cheapest_products': cheapest_products})