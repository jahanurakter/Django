from django.db import models
from django.contrib.auth.models import User


class AddCashModel(models.Model):
    cash_name=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True
        )
    source=models.CharField(max_length=150, null=True)
    datetime=models.DateField(auto_now_add=True, null=True)
    cash_amount=models.PositiveIntegerField(null=True)
    cash_description=models.TextField(null=True)
    
    def __str__(self):
        return f"{self.source}"

class ExpenseModel(models.Model):
    expense_name=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True
        )
    datetime=models.DateField(null=True)
    expense_amount=models.PositiveIntegerField(null=True)
    expense_description=models.TextField(null=True)

    def __str__(self):
        return f"{self.expense_name}"



    # https://limewire.com/d/js89k#CbTk1E0fut