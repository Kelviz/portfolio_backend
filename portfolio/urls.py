from django.urls import path, include
from rest_framework import routers
from .views import AboutViewSet, TagViewSet, WorkViewSet, SkillViewSet, YearExperienceViewSet, TestimonialViewSet, SendMessageViewSet

router = routers.DefaultRouter()

router.register("about", AboutViewSet, basename="about")
router.register("tags", TagViewSet, basename="tags")
router.register("works", WorkViewSet, basename="works")
router.register("skills", SkillViewSet, basename="skills")
router.register("years", YearExperienceViewSet, basename="years")
router.register("testimonials", TestimonialViewSet, basename="testimonials")
router.register("contact", SendMessageViewSet, basename="contact")

urlpatterns = [
    path('', include(router.urls))

]
