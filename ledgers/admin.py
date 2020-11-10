from django.contrib import admin

from ledgers.models import Ledger


@admin.register(Ledger)
class LedgerAdmin(admin.ModelAdmin):
    list_display = ("get_acct_owner", "account_number", "balance",)

    def get_acct_owner(self, obj):
        return f"{obj.user}"

    get_acct_owner.short_description = "Client Name"
