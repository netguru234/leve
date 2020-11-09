from django.db import models


class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    checkbox = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.full_name} - {self.subject}"
