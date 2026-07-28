from django.shortcuts import render
from rest_framework import viewsets

from ecosystem_foundations.base.views import (
    ActiveQuerysetMixin,
    BaseItemTypeQueryViewSetMixin,
    BaseQueryViewSetMixin,
    GenericTargetQuerysetMixin,
    TimeAuditableQuerysetMixin,
)

from .models import Alert, AlertStatusItem
from .serializers import (
    AlertSerializer,
    AlertStatusItemSerializer,
)


# Create your views here.


# -------------------------------------------------
# Alert Status Types
# -------------------------------------------------

class AlertStatusItemViewSet(
    ActiveQuerysetMixin,
    BaseItemTypeQueryViewSetMixin,
    BaseQueryViewSetMixin,
    viewsets.ModelViewSet,
):
    queryset = AlertStatusItem.objects.all()
    serializer_class = AlertStatusItemSerializer


# -------------------------------------------------
# Alerts
# -------------------------------------------------

class AlertViewSet(
    ActiveQuerysetMixin,
    TimeAuditableQuerysetMixin,
    GenericTargetQuerysetMixin,
    BaseQueryViewSetMixin,
    viewsets.ModelViewSet,
):
    queryset = Alert.objects.select_related(
        "status",
        "content_type",
    )

    serializer_class = AlertSerializer