from django.db import models

from order.constants import OrderStatusChoices

class Order(models.Model):
    client_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=14, null=True)
    status = models.SmallIntegerField(choices=OrderStatusChoices.choices, default=OrderStatusChoices.NEW)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.client_name

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='orders')
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f"# Order ID: {self.order.id}"


