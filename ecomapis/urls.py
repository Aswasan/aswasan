from django.urls import path, include
from .views import *

urlpatterns = [
    path('get-product/',getProducts),
    path('add-product/', addProducts),
    path('single-product-detail/<int:product_id>', singleproductDetail),
    path('edit-product/<int:product_id>', editProduct),
    path('delete-product/<int:product_id>', deleteProduct),
]