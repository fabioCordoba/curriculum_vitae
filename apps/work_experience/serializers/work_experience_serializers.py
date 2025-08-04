from rest_framework import serializers

from apps.work_experience.models.work_experience import WorkExperience


class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = [
            "position",
            "company_name",
            "start_year",
            "end_year",
            "description",
            "is_current",
        ]
