from rest_framework import serializers

from apps.contact.serializer.contact_serializers import ContactSerializer
from apps.curriculum.models.curriculum import Curriculum
from apps.skill.serializers.skill_serializers import SkillSerializer
from apps.users.serializers.user_serializers import UserSerializer


class CurriculumSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    contact = ContactSerializer(read_only=True)
    skills = SkillSerializer(many=True, read_only=True)

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
            "created_at",
            "updated_at",
        ]
