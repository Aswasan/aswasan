from django.shortcuts import render
from ecommerce.models import *
from rest_framework.response import Response
from .serializer import *
from rest_framework.decorators import api_view
# Create your models here.

@api_view(['GET'])
def getProducts(request):
    try:
      products= Product.objects.all()
      serializers_data = ProductSerializer(products,many=True)
      return Response(serializers_data.data)
    except Exception as e:
       return Response({'err':e})
    
@api_view(['GET'])
def singleproductDetail(request, product_id):
   products = Product.objects.get(pk=product_id)
   serialized_json = ProductSerializer(products,many=False)
   return Response(serialized_json.data)

@api_view(['POST'])
def addProducts(request):
  request_data = request.data
  serializer_data = ProductSerializer(data =request_data, many=False)
  if serializer_data.is_valid(raise_exception=True):
      serializer_data.save()
      return Response({'message':'Product added successfully'})

@api_view(['POST'])
def editProduct(request, product_id):
   product = Product.objects.get(pk=product_id)
   serialized_data = ProductSerializer(product,data = request.data, many = False, partial=True)
   if serialized_data.is_valid(raise_exception=True):
    serialized_data.save()
    return Response({'message':'Product Updated Successfully'})

@api_view(['GET'])
def deleteProduct(Request, product_id):
   product = Product.objects.get(pk= product_id)
   product.delete()
   return Response({'message':'Product deleted successfully'})
   

         