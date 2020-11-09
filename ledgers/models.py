from django.db import models

from core.models import AbstractTimeStamp
from users.models import User


class Ledger(AbstractTimeStamp):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_ledger")
    account_number = models.BigIntegerField()
    balance = models.DecimalField(default=0.00, decimal_places=2, max_digits=10000000000)

    def __str__(self):
        return f"Account Number: {self.account_number} / Balance: ${self.balance}"
