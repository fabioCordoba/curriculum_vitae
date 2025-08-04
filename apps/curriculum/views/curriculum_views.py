from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin

from apps.curriculum.models.curriculum import Curriculum
from apps.curriculum.serializers.curriculum_serializers import CurriculumSerializer


class CurriculumViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Curriculum.objects.all()  # type: ignore
    serializer_class = CurriculumSerializer
    lookup_field = "pk"
