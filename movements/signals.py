from django.db.models.signals import post_save
from django.dispatch import receiver
from django.apps import apps
from .models import StockMovement

@receiver(post_save, sender=StockMovement)
def product_inventory_update(sender, instance, created, **kwargs):
    if created:
        ProductInventory = apps.get_model('products', 'ProductInventory')
        product = instance.product
        quantity = instance.quantity
        movement_type = instance.movement_type

        try:
            inventory = ProductInventory.objects.get(product=product)
        except ProductInventory.DoesNotExist:
            inventory = ProductInventory.objects.create(product=product, product_quantity=0)

        if movement_type == 'PURCHASE':
            inventory.product_quantity += quantity
            inventory.transaction_type = 'PURCHASE'

        elif movement_type == 'SALE':
            inventory.product_quantity -= quantity
            inventory.transaction_type = 'SALE'

        elif movement_type == 'ADJUSTMENT':
            inventory.product_quantity += quantity
            inventory.transaction_type = 'ADJUSTMENT'

        inventory.save()