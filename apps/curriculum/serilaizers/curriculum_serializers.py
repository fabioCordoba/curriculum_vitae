from rest_framework import serializers

from apps.curriculum.models.curriculum import Curriculum
from apps.users.serializers.user_serializers import UserSerializer


class CurriculumSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Curriculum
        fields = [
            "id",
            "name",
            "position",
            "profession",
            "profile",
            "user",
            "created_at",
            "updated_at",
        ]
