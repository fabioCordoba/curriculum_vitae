from django.contrib import admin

from apps.education.models.education import Education


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ["name", "start_year", "end_year", "status"]
