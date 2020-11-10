from django.db import models


class SiteInfo(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.address} -  {self.phone} - {self.email}"
