from django.contrib import admin

from ledgers.models import Ledger
from transactions.models import Transaction, Wire
from django.contrib.auth.models import User


@admin.register(Transaction, Wire)
class TransactionAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if obj.transaction_type == "debit":
            user = User.objects.filter(username=obj.acct_owner).first()
            user_balance = user.user_ledger.balance - obj.amount
            user.user_ledger.balance = user_balance
            user.user_ledger.save()

        if obj.transaction_type == "credit":
            user = User.objects.filter(username=obj.acct_owner).first()
            user_balance = user.user_ledger.balance + obj.amount
            user.user_ledger.balance = user_balance
            user.user_ledger.save()

        if obj.transaction_type == "wire":
            user = User.objects.filter(username=obj.acct_owner).first()
            user_balance = user.user_ledger.balance - obj.amount
            user.user_ledger.balance = user_balance
            user.user_ledger.save()

        super().save_model(request, obj, form, change)

