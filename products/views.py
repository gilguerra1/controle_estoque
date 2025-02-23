from rest_framework import generics
from products.models import Product, ProductInventory
from products.serializers import ProductSerializer, ProductInventorySerializer


class ProductCreateListView(generics.ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetriveUpdateDetroyView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductInventoryListView(generics.ListCreateAPIView):

    queryset = ProductInventory.objects.all()
    serializer_class = ProductInventorySerializer
