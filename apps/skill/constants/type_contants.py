from django.db import models


class TypeChoices(models.TextChoices):

    LANGUAGES = "Lenguajes de Programación", "Programming Languages"
    FRAMEWORK = "Framework", "Framework"
    DATABASES = "Bases de Datos", "Databases"
    TOOLS = "Herramientas", "Tools"
    OTHERS = "Otros", "Others"
