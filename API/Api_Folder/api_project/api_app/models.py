from django.db import models

class ProductModel(models.Model):
    name=models.CharField(max_length=100, null=True)
    description=models.TextField(null=True)
    price=models.PositiveIntegerField(null=True)
    qty=models.PositiveIntegerField(null=True)

    def __str__(self): 
        return f"{self.name}"