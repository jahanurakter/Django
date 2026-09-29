from django.db import models
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):
    name=models.CharField(max_length=100, null=True)
    email=models.EmailField(null=True)
    phone=models.IntegerField(null=True)

    def __str__(self):
        return f"{self.name}"

class ProductModel(models.Model):
    p_name=models.CharField(max_length=100, null=True)
    description=models.TextField(null=True)
    price=models.PositiveIntegerField(null=True)
    image=models.ImageField(upload_to='media/product_img',null=True)
    user=models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.p_name}"

    
