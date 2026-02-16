from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    min_num = 1
    max_num=10
    extra = 0
    readonly_fields = ('product_stock_display',)  # stock ko‘rinishi
    fields = ('product', 'product_stock_display', 'quantity',)


    def product_stock_display(self, obj):
        return f"{obj.product.stock} {obj.product.get_unit_display()}"

    product_stock_display.short_description = 'Qolgan stock'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'status', 'created_at')
    list_filter = ('status', 'created_at',)
    search_fields = ('client_name',)
    inlines = [OrderItemInline]
