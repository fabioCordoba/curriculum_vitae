from rest_framework import serializers

from apps.contact.serializer.contact_serializers import ContactSerializer
from apps.curriculum.models.curriculum import Curriculum
from apps.education.serializers.education_serializers import EducationSerializer
from apps.portfolio.serializers.portfolio_serializers import PortfolioSerializer
from apps.skill.serializers.skill_serializers import SkillSerializer
from apps.users.serializers.user_serializers import UserSerializer
from apps.work_experience.serializers.work_experience_serializers import (
    WorkExperienceSerializer,
)


class CurriculumSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    contact = ContactSerializer(read_only=True)
    skills = SkillSerializer(many=True, read_only=True)
    educations = EducationSerializer(many=True, read_only=True)
    work_experiences = WorkExperienceSerializer(many=True, read_only=True)
    portfolios = PortfolioSerializer(many=True, read_only=True)

    class Meta:
        model = Curriculum
        fields = [
            "id",
            "name",
            "position",
            "profession",
            "profile",
            "user",
            "contact",
            "skills",
            "educations",
            "work_experiences",
            "portfolios",
            "created_at",
            "updated_at",
        ]
