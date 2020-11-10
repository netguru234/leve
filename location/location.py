from pages.models import SiteInfo


def sitemap():
    location = SiteInfo.objects.last()
    data = {
        "site_info": location
    }
    return data
