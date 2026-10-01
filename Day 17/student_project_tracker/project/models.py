from django.db import models
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):
    TYPES=[
        ('Vendor','Vendor'),
        ('Customer','Customer')
    ]
    user_type=models.CharField(choices=TYPES, max_length=150, null=True)
    
    def __str__(self):
        return f"{self.username}"

class VendorProfileModel(models.Model):
    user_info=models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        related_name='vendor_profile'
    )
    company_name=models.CharField(max_length=150, null=True)
    company_logo=models.ImageField(upload_to='media/logo', null=True)
    address=models.CharField(max_length=150, null=True)
    phone=models.CharField(max_length=20, null=True)

    def __str__(self):
        return f"{self.company_name}"

    
class CustomerProfileModel(models.Model):
    user_info=models.OneToOneField(
            UserModel,
            on_delete=models.CASCADE,
            related_name='customer_profile',
            null=True
        )
    customer_name=models.CharField(max_length=150, null=True)
    address=models.TextField(null=True)
    phone=models.CharField(max_length=100, null=True)
    customer_image=models.ImageField(upload_to='media/project_img', null=True)
    membership=models.CharField(max_length=150,null=True)
    def __str__(self):
        return f"{self.customer_name}"