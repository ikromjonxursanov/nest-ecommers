from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import RegexValidator
from order.constants import OrderStatusChoices

phone_validator = RegexValidator(
    regex=r'^\+998\d{9}$',
    message="Telefon raqam +998 bilan boshlanib, 9 ta raqamdan iborat bo‘lishi kerak")



class Order(models.Model):
    client_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13,validators=[phone_validator], unique=True)
    status = models.SmallIntegerField(choices=OrderStatusChoices.choices, default=OrderStatusChoices.NEW)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.client_name


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='orders',
                                limit_choices_to={"is_active": True})
    quantity = models.FloatField(default=1)

    def clean(self):
        if self.quantity <= 0:
            raise ValidationError({"quantity": "Faqat musbat son bo'lishi kerak"})
        elif self.quantity > self.product.stock:
            raise ValidationError({"quantity": "Buncha mahsulot yo'q"})

    def save(self, *args, **kwargs):
        if not self.pk:
            self.product.stock -= self.quantity
            self.product.save()
        else:
            old_order_item = OrderItem.objects.get(pk=self.pk)
            if old_order_item.quantity != self.quantity:
                self.product.stock += old_order_item.quantity
                self.product.stock -= self.quantity
                self.product.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"# Order ID: {self.order.id}"