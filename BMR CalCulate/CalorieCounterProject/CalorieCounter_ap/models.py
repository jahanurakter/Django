from django.db import models
from django.contrib.auth.models import User

class UserProfileModel(models.Model):
    GENDER={
        ('Female','Female'),
        ('Male','Male'),
    }
    user=models.OneToOneField(
        User,
            on_delete=models.CASCADE,
            max_length=100,
            related_name='user_profile',
            null=True
    )
    name=models.CharField(max_length=150,null=True)
    age=models.PositiveIntegerField(null=True)
    gender=models.CharField(choices=GENDER, max_length=50, null=True)
    height=models.FloatField(null=True)
    weight=models.FloatField(null=True)
    bmr=models.FloatField(null=True)
    image=models.ImageField(upload_to='media/image', null=True)

    def __str__(self):
        return f"{self.name}"

class ConsumedCalorieModel(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        max_length=100,
        related_name='calorie_consumed',
        null=True
    )
    item_name=models.CharField(max_length=150, null=True)
    consumed_calorie=models.FloatField(null=True)

    def __str__(self):
        return f"{self.user.username}-{self.item_name}"
