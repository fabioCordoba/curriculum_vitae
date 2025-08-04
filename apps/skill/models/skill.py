from django.db import models

from apps.core.models.base_model import BaseModel
from apps.curriculum.models.curriculum import Curriculum
from apps.skill.constants.type_contants import TypeChoices


class Skill(BaseModel):
    curriculum = models.ForeignKey(
        Curriculum,
        on_delete=models.CASCADE,
        related_name="skills",
    )
    name = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(
        max_length=50,
        choices=TypeChoices.choices,
        null=True,
        blank=True,
        default=TypeChoices.LANGUAGES,
    )
