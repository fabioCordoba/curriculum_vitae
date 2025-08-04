from django.contrib import admin

from apps.skill.models.skill import Skill


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ["name"]
