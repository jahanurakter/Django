from django.db import models
from django.contrib.auth.models import User


class SupplierModel(models.Model):
    user=models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='supplier_name',
        null=True
    )
    supplier_name=models.CharField(max_length=150, null=True)
    contact_number=models.CharField(max_length=50,null=True)
    address=models.TextField(null=True)

    def __str__(self):
        return f"{self.supplier_name}"
    

class UserProfileModel(models.Model):
    user=models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='user_profile',
        null=True
    )
    full_name=models.CharField(max_length=150, null=True)
    phone=models.PositiveIntegerField(null=True)
    address=models.TextField(null=True)
    picture=models.ImageField(upload_to='media/user_image', null=True)

    def __str__(self):
        return f"{self.full_name}"


class PurchaseModel(models.Model):
    user=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_purchase',
        null=True    
    )
    user_supplier=models.ForeignKey(
        SupplierModel,
        on_delete=models.CASCADE,
        related_name='supplier_purchase',
            null=True
    )
    product_name=models.CharField(max_length=150, null=True)
    quantity=models.PositiveIntegerField(null=True)
    unitprice=models.FloatField(null=True)
    discount=models.FloatField(null=True)
    paid_amount=models.FloatField(null=True)
    purchase_date=models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.username}-{self.product_name}"
    