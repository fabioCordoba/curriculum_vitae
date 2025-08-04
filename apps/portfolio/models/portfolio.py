from django.db import models

from apps.core.models.base_model import BaseModel
from apps.curriculum.models.curriculum import Curriculum
from apps.portfolio.constants.category_constants import CategoryChoices


class Portfolio(BaseModel):
    curriculum = models.ForeignKey(
        Curriculum,
        on_delete=models.CASCADE,
        related_name="portfolios",
    )
    name = models.CharField(max_length=100, null=True, blank=True)
    category = models.CharField(
        max_length=20, choices=CategoryChoices.choices, default=CategoryChoices.OTHERS
    )
    description = models.TextField(blank=True)
    repository = models.CharField(max_length=100, null=True, blank=True)
    demo = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(
        upload_to="portfolio/",  # 📂 se guarda en MEDIA_ROOT/portfolio/
        null=True,
        blank=True,
    )
