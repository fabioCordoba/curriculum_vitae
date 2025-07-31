from django.contrib import admin

from apps.curriculum.models.curriculum import Curriculum


@admin.register(Curriculum)
class CurriculumAdmin(admin.ModelAdmin):
    list_display = ["name"]
