from django.db import models
from django.contrib.auth.models import AbstractUser

class AbstractModel(AbstractUser):

    USER_TYPE=[
        ('Fruits','Fruits'),
        ('Grocery','Grocery'),
        ('Fashion','Fashion')
    ]
    image=models.ImageField(upload_to='media/product_img', null=True)
    user_type=models.CharField(choices=USER_TYPE, max_length=20, null=True)


    def __str__(self):
        return f"{self.name}"

class ProductModel(models.Model):
    name=models.CharField(max_length=100, null=True)
    phone=models.CharField(max_length=100, null=True)
    price=models.PositiveIntegerField(null=True)
    created_by=models.ForeignKey(AbstractModel, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True, null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return f"{self.name}"

    