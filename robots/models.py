from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from orders.models import Order
from orders.service import generate_letter_and_send_mail


class Robot(models.Model):
    serial = models.CharField(max_length=5, blank=False, null=False)
    model = models.CharField(max_length=2, blank=False, null=False)
    version = models.CharField(max_length=2, blank=False, null=False)
    quantity = models.IntegerField(default=0, blank=False, null=False)
    created = models.DateTimeField(blank=False, null=False)
    
    
@receiver(post_save, sender=Robot)
def send_notification(sender, instance, **kwargs):
    '''Сигнал на изменеие модели и проверки значения quantity'''
    if hasattr(instance, '_previous_quantity'):
        previous_quantity = instance._previous_quantity
    else:
        previous_quantity = 0
    if previous_quantity == 0 and instance.quantity > 0:
        matching_orders = Order.objects.filter(robot_serial=f"{instance.model}-{instance.version}")
        email_addresses = [order.customer.email for order in matching_orders]
        generate_letter_and_send_mail(email_addresses, instance.model, instance.version)
