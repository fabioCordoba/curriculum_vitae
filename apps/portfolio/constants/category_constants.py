from django.db import models


class CategoryChoices(models.TextChoices):
    FRONTEND = "Frontend", "Frontend"
    BACKEND = "Backend", "Backend"
    OTHERS = "Otros", "Others"
