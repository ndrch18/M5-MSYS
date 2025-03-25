from django.shortcuts import render
from .models import WaterBottle, Supplier

# Create your views here.

def view_bottles(request):
    bottle_objects = WaterBottle.objects.all()
    return render(request, 'MyInventoryApp/view_bottles.html', {'bottles':bottle_objects})

def view_supplier(request):
    supplier_objects = Supplier.objects.all()
    return render(request, 'MyInventoryApp/view_supplier.html', {'supplier':supplier_objects})

def add_bottle(request):
    return render(request, 'MyInventoryApp/add_bottle.html')