from django.db import models
from django.contrib.auth.models import AbstractUser

class AbstractModel(AbstractUser):
    USER_TYPE=[
        ('Customer','Customer'),
        ('Vendor', 'Vendor')
    ]
    image=models.ImageField(upload_to='media/profile_img', null=True)
    user_type=models.CharField(choices=USER_TYPE,max_length=20 ,null=True)

    def __str__(self):
        return f"{self.username}"