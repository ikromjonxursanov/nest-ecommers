from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    min_num = 1
    max_num = 3

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('client_name',  'status', 'created_at')
    list_filter = ('status', 'created_at',)
    search_fields = ('client_name',)
    inlines = [OrderItemInline]

