# views.py
from rest_framework import viewsets
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from django.shortcuts import render
import csv
from django.http import HttpResponse


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

def home_view(request):
    return render(request,template_name="home.html")

def export_products_csv(request):
    # Create the HttpResponse object with CSV header
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=products.csv'

    writer = csv.writer(response)
    writer.writerow(['ID', 'Name', 'Description', 'Price', 'Category'])

    products = Product.objects.all()
    for product in products:
        writer.writerow([product.id, product.name, product.description, product.price, product.category.name])

    return response



