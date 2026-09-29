from django.db import models

class ProductModel(models.Model):
    PRODUCT_TYPE=[
            ('fruits', 'Fruits'),
            ('grocery', 'Grocery'),
            ('fashion', 'Fashion'),
        ]
     
    name=models.CharField(max_length=150, null=True)
    description=models.TextField(null=True)
    price=models.PositiveIntegerField(null=True)
    product_date=models.DateField(null=True)
    image=models.ImageField(upload_to="media/product_img", null=True)
    product_type=models.CharField(choices=PRODUCT_TYPE,max_length=20, null=True)
    created_at=models.DateTimeField(auto_now_add=True, null=True)
    updated_at=models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.name}"