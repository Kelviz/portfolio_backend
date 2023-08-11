from django.urls import path, include
from rest_framework import routers
from .views import AboutViewSet, TagViewSet, WorkViewSet

router = routers.DefaultRouter()

router.register("about", AboutViewSet, basename="about")
router.register("tags", TagViewSet, basename="tags")
router.register("works", WorkViewSet, basename="works")

urlpatterns = [

    path('', include(router.urls))

]
