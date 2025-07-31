from django.db import models
from apps.core.models.base_model import BaseModel


class Curriculum(BaseModel):
    name = models.CharField(max_length=100)
    profile = models.TextField(blank=True)
