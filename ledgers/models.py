from django.db import models

from core.models import AbstractTimeStamp
from django.contrib.auth.models import User


class Ledger(AbstractTimeStamp):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_ledger")
    account_number = models.BigIntegerField()
    balance = models.DecimalField(decimal_places=2, max_digits=19)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return f"Account Number: {self.account_number} / Balance: ${self.balance}"
