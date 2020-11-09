from django.contrib import admin

from ledgers.models import Ledger


@admin.register(Ledger)
class LedgerAdmin(admin.ModelAdmin):
    pass
