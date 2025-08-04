from django.db import models


class StatusChoices(models.TextChoices):
    IN_PROGRESS = "in_progress", "En curso"
    COMPLETED = "completed", "Finalizado"
    INCOMPLETE = "incomplete", "Incompleto"
    PAUSED = "paused", "En pausa"
    CERTIFIED = "certified", "Certificado"
