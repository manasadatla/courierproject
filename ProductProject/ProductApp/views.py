from django.shortcuts import render

# Create your views here.
from ProductApp.models import ProductDetails


def to_calculate_volume(request):
    product_data=ProductDetails.objects.all()
    for product in product_data:
        product.volume=product.cost_per_item*product.stock_quantity
    return render(request=request,template_name='display.html',context={'product_data':product_data})