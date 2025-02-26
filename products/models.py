from django.db import models
from suppliers.models import Supplier
from categories.models import Category
from movements.models import StockMovement


class Product(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='product_category')
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, related_name='product_supplier')
    barcode = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class ProductInventory(models.Model):

    product = models.ForeignKey('products.Product', on_delete=models.PROTECT, related_name='inventory_product')
    product_quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
