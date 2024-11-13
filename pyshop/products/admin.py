from django.contrib import admin
from .models import Product, Order
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


admin.site.register(Product,ProductAdmin)
admin.site.register(Order)