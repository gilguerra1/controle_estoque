from rest_framework import serializers
from products.models import Product, ProductInventory


class ProductSerializer(serializers.ModelSerializer):

    class Meta:

        model = Product
        fields = '__all__'


class ProductInventorySerializer(serializers.ModelSerializer):

    class Meta:

        model = ProductInventory
        fields = '__all__'
