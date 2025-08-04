from django.db import models
from apps.core.models.base_model import BaseModel


class Curriculum(BaseModel):
    user = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        verbose_name="user",
        related_name="user_cv",
    )
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    profile = models.TextField(blank=True)

    class Meta:
        verbose_name = "Curriculum"
        verbose_name_plural = "Curriculums"
        ordering = ("created_at",)

    def __str__(self):
        return f"Curriculum: {self.name}"
