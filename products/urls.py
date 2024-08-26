
from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.get_all_products, name='get_product'),
    path('add-prduct/', views.add_product, name='add_product'),
    path('product-details/<int:product_id>/', views.get_single_product, name='product_details'),
    path('delete-product/<int:product_id>/', views.delete_product, name='delete_product'),
]
