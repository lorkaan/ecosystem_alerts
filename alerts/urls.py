from rest_framework.routers import DefaultRouter

from .views import (
    AlertStatusItemViewSet,
    AlertViewSet,
)


router = DefaultRouter()


router.register(
    r"",
    AlertViewSet,
    basename="alert"
)


router.register(
    r"statuses",
    AlertStatusItemViewSet,
    basename="alert-status"
)


urlpatterns = router.urls