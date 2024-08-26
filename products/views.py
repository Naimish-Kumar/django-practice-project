from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product
import json

def get_all_products(request):
    products = Product.objects.all().values()
    return JsonResponse(list(products), safe=False)

def get_single_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        return JsonResponse({
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': product.price,
        })
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)

@csrf_exempt
def add_product(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product = Product.objects.create(
            name=data['name'],
            description=data['description'],
            price=data['price']
        )
        return JsonResponse({
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': product.price,
        }, status=201)
    return JsonResponse({'error': 'Invalid request method'}, status=400)

@csrf_exempt
def delete_product(request, product_id):
    if request.method == 'DELETE':
        try:
            product = Product.objects.get(id=product_id)
            product.delete()
            return JsonResponse({'message': 'Product deleted successfully'}, status=200)
        except Product.DoesNotExist:
            return JsonResponse({'error': 'Product not found'}, status=404)
    return JsonResponse({'error': 'Invalid request method'}, status=400)
