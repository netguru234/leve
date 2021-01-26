from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models

from core.models import AbstractTimeStamp


class SiteInfo(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.address} -  {self.phone} - {self.email}"


class Document(AbstractTimeStamp):
    RECEIPT = "receipt"
    GOVT_ID = "govt_id"
    PASSPORT = "passport"

    DOCUMENT_CHOICES = (
        (RECEIPT, "Receipt"),
        (GOVT_ID, "Government ID"),
        (PASSPORT, "Passport Photograph"),
    )

    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    document = models.ImageField(upload_to="uploads/docs",
                                 validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])
    document_type = models.CharField(max_length=100, choices=DOCUMENT_CHOICES)

    @property
    def get_created_at(self):
        return self.created_at.strftime("%m/%d/%Y, %H:%M:%S")

    def __str__(self):
        return f"{self.uploaded_by.get_full_name()} ({self.document_type})  - {self.get_created_at}"
