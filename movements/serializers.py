from rest_framework import serializers
from movements.models import StockMovement
from products.models import ProductInventory


class StockMovementSerializer(serializers.ModelSerializer):

    class Meta:

        model = StockMovement
        fields = '__all__'

    def validate_quantity(self, value):
        data = self.context['request'].data
        movement_type = data.get('movement_type')
        product_id = data.get('product')

        if movement_type == 'SALE':

            try:
                inventory = ProductInventory.objects.get(product_id=product_id)
                if value > inventory.product_quantity:
                    raise serializers.ValidationError(f'Quantidade insuficiente em estoque. {inventory.product_quantity} unidades disponíveis em estoque! ')
            except ProductInventory.DoesNotExist:
                raise serializers.ValidationError('Produto não encontrado no inventário.')

        elif movement_type == 'ADJUSTMENT' and value < 0:

            raise serializers.ValidationError('A quantidade de ajuste não pode ser negativa.')

        elif movement_type == 'PURCHASE' and value < 0:

            raise serializers.ValidationError('A quantidade de compra não pode ser negativa.')
        
        return value
