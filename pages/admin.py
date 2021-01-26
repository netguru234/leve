from django.contrib import admin

from pages.models import SiteInfo, Document

admin.site.register(SiteInfo)


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    pass
