from rest_framework import serializers

from apps.skill.models.skill import Skill


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ["id", "name", "type"]
