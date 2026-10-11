from django.db import models
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):
    CATEGORY = [
        ('Vendor','Vendor'),
        ('Customer','Customer'),
    ]
    user_type=models.CharField(choices=CATEGORY, max_length=50, null=True)
    full_name=models.CharField(max_length=100, null=True)
    def __str__(self):
        return f"{self.username}"
    
class CustomerModel(models.Model):
    name=models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.name}"

class ProductModel(models.Model):
    p_name=models.CharField(max_length=100, null=True)
    p_details=models.TextField(null=True)
    price=models.PositiveIntegerField(null=True)
    qty=models.PositiveIntegerField(null=True)
    total_amount=models.FloatField(null=True)
    category=models.ForeignKey(
        CustomerModel,
        on_delete=models.SET_NULL,
        related_name='product_category', null=True
    )
    created_by=models.ForeignKey(
        UserModel,
    on_delete=models.CASCADE,
    related_name='product_user', null=True)
    created_at=models.DateTimeField(auto_now_add=True, null=True)
    update_at=models.DateField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.name}"
