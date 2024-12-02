from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from orders.forms import OrderForm
from products.models import Product
from orders.models import Order

@login_required
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            order.products.set(Product.objects.filter(id__in=request.POST.getlist('products')))
            return redirect('product_list')
    else:
        form = OrderForm()
    products = Product.objects.all()
    return render(request, 'orders/create_order.html', {'form': form, 'products': products})
