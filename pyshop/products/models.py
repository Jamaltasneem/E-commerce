from django.db import models
from django.contrib.auth.models import User
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    delivery_address = models.TextField()
    PAYMENT_METHOD_CHOICES = [
        ('COD', 'Cash on Delivery'),
    ]
    payment_method = models.CharField(max_length=3, choices=PAYMENT_METHOD_CHOICES, default='COD')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Order {self.id} by {self.user.username} for {self.product.name}"
