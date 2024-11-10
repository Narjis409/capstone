from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Orders, Meals
from .forms import OrderForm  

def order_list(request):
    orders = Orders.objects.all()
    return render(request, 'order_list.html', {'orders': orders})


def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'order_form.html', {'form': form})


def order_detail(request, pk):
    order = get_object_or_404(Orders, pk=pk)
    return render(request, 'order_detail.html', {'order': order})
