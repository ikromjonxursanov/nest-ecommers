from django.db import models
from django.utils.text import slugify

class Product(models.Model):
    UNIT_CHOICES=(
        ('pcs', 'Dona'),
        ('kg', 'Kilogram')
    )
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField(blank=True, null=True)
    stock = models.FloatField(default=0)
    unit = models.CharField(max_length=3, choices=UNIT_CHOICES, default='pcs')
    is_active = models.BooleanField(default=True)
    price = models.FloatField(default=0)
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.stock <= 0:
            self.is_active = False
        elif not self.is_active and self.stock > 0:
            self.is_active = True

        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


