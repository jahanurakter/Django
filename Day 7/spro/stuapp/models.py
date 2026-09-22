from django.db import models

class stuinfo(models.Model):
    name=models.CharField(max_length=150,verbose_name="Student Name")
    address=models.TextField()
    email=models.EmailField(default="a@gmail.com")
    age=models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name}"

