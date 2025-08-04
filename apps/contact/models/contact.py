from django.db import models
from apps.core.models.base_model import BaseModel
from phonenumber_field.modelfields import PhoneNumberField

from apps.curriculum.models.curriculum import Curriculum


class Contact(BaseModel):
    curriculum = models.OneToOneField(
        Curriculum, on_delete=models.CASCADE, related_name="contact"
    )
    email = models.EmailField(unique=True, null=False, blank=False)
    phone_number = PhoneNumberField(null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    web = models.CharField(max_length=100, null=True, blank=True)
    linkendin = models.CharField(max_length=100, null=True, blank=True)
    github = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
        ordering = ("created_at",)

    def __str__(self):
        return f"Contact: {self.email}"
