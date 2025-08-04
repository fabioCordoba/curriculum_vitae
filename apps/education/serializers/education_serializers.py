from rest_framework import serializers

from apps.education.models.education import Education


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ["start_year", "end_year", "description", "status"]
