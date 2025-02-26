import smtplib
import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from movements.models import StockMovement
from products.models import ProductInventory
from .emails import product_inventory_email


logger = logging.getLogger(__name__)

@receiver(post_save, sender=StockMovement)
def alert_stock_quantity(sender, instance, created, **kwargs):
    if created or instance.movement_type == 'SALE':
        try:
            inventory = ProductInventory.objects.get(product=instance.product)
            
            if inventory.product_quantity < 10:
                subject = f"Alerta de Estoque Baixo: {instance.product.name}"
                message = f"""
                    <html>
                    <body>
                        <h2>Alerta de Estoque Baixo</h2>
                        <p><strong>Produto:</strong> {instance.product.name}</p>
                        <p><strong>Quantidade em Estoque:</strong> {inventory.product_quantity}</p>
                        <p><strong>Data da Venda:</strong> {instance.movement_date.strftime('%d/%m/%Y %H:%M')}</p>
                    </body>
                    </html>
                """
                product_inventory_email(subject, message)

        except ProductInventory.DoesNotExist:
            logger.error(f"ProductInventory não encontrado para o produto {instance.product.name}")
        except smtplib.SMTPException as e:
            logger.error(f"Erro ao enviar e-mail: {e}")
        except Exception as e:
            logger.error(f"Erro inesperado: {e}")
