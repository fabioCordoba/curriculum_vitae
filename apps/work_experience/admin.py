from django.contrib import admin

from apps.work_experience.models.work_experience import WorkExperience


@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ["position", "company_name", "start_year", "end_year", "is_current"]
