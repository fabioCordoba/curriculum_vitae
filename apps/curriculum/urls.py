from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.curriculum.views.curriculum_views import CurriculumViewSet

router = DefaultRouter()
router.register(r"curriculums", CurriculumViewSet, basename="curriculum")

urlpatterns = router.urls
