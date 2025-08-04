from django.db import models

from apps.core.models.base_model import BaseModel
from apps.curriculum.models.curriculum import Curriculum
from apps.education.constants.status_constants import StatusChoices


class Education(BaseModel):
    curriculum = models.ForeignKey(
        Curriculum,
        on_delete=models.CASCADE,
        related_name="educations",
    )
    name = models.CharField(max_length=100, null=True, blank=True)
    start_year = models.PositiveIntegerField(null=True, blank=True)
    end_year = models.PositiveIntegerField(null=True, blank=True)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=20, choices=StatusChoices.choices, default=StatusChoices.IN_PROGRESS
    )
