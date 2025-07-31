from django.db import models


class Curriculum(models.Model):
    name = models.CharField(max_length=100)
    profile = models.TextField(blank=True)
