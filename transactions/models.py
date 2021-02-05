from django.contrib.auth.models import User
from django.db import models
from django.forms import forms
from django_countries.fields import CountryField

from core.models import AbstractTimeStamp


class Wire(AbstractTimeStamp):
    acct_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_tfs")
    amount = models.DecimalField(decimal_places=2, max_digits=19)
    bank_name = models.CharField(max_length=100)
    acct_num = models.CharField(max_length=50)
    swift_code = models.CharField(max_length=50)
    bank_address = models.CharField(max_length=255)
    bank_phone = models.CharField(max_length=20)
    country = CountryField()
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=20)
    recipient = models.CharField(max_length=100)
    transaction_type = models.CharField(max_length=100, default="wire")
    tf_code = models.IntegerField()

    def __str__(self):
        return f"{self.recipient} - ${self.amount} ({self.transaction_type}) - (Transfer Code: {self.tf_code})"

    class CustomForm(forms.Form):
        country = CountryField().formfield()

    class Meta:
        ordering = ("-created_at",)


class Transaction(AbstractTimeStamp):
    DEBIT = "debit"
    CREDIT = "credit"

    TRANSACTION_CHOICES = (
        (DEBIT, "Debit"),
        (CREDIT, "Credit"),
    )

    transaction_type = models.CharField(max_length=30, choices=TRANSACTION_CHOICES)
    acct_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_transactions")
    amount = models.DecimalField(decimal_places=2, max_digits=19)

    def __str__(self):
        return f"{self.acct_owner} - ${self.amount} ({self.transaction_type})"
