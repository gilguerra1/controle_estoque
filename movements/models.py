from django.db import models


MOVEMENT_TYPE = (
    ('SALE', 'Saída'),
    ('PURCHASE', 'Entrada'),
    ('ADJUSTMENT', 'Ajuste')
)


class StockMovement(models.Model):

    product = models.ForeignKey('products.Product', on_delete=models.PROTECT, related_name='stock_movements')
    quantity = models.IntegerField()
    movement_type = models.CharField(
        max_length=10,
        choices=MOVEMENT_TYPE,
    )
    movement_date = models.DateTimeField(auto_now_add=True)
