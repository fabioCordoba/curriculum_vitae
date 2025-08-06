from rest_framework import serializers
from apps.portfolio.models.portfolio import Portfolio


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = [
            "name",
            "category",
            "description",
            "repository",
            "demo",
            "image",
            "created_at",
        ]
