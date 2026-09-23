from django.db import models

class ProductModel(models.Model):

    name=models.CharField(max_length=150, null=True)
    description=models.TextField(null=True)
    price=models.PositiveIntegerField(null=True)
    product_date=models.DateField(null=True)
    image=models.ImageField(upload_to="media/product_img", null=True)