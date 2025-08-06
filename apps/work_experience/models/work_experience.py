from django.db import models
from django.core.exceptions import ValidationError

from apps.core.models.base_model import BaseModel
from apps.curriculum.models.curriculum import Curriculum


class WorkExperience(BaseModel):
    curriculum = models.ForeignKey(
        Curriculum,
        on_delete=models.CASCADE,
        related_name="work_experiences",
    )
    position = models.CharField(max_length=100, null=True, blank=True)
    company_name = models.CharField(max_length=100, null=True, blank=True)
    start_year = models.PositiveIntegerField(null=True, blank=True)
    end_year = models.PositiveIntegerField(null=True, blank=True)
    description = models.TextField(blank=True)
    is_current = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def clean(self):
        if self.end_year and self.end_year < self.start_year:
            raise ValidationError(
                "El año de finalizacion no puede ser anterior al de inicio"
            )
        if self.is_current and self.end_year:
            raise ValidationError(
                "No puedes tener un año de finalizacion si aun estas trabajando aqi."
            )
        return super().clean()
