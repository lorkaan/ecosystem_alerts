from rest_framework import serializers

from foundations.ecosystem_foundations.base.serializers import (
    BaseItemTypeSerializerMixin,
    ActiveSerializerMixin,
    TimeAuditableSerializerMixin,
    GenericTargetField,
)

from .models import AlertStatusItem, Alert


class AlertStatusItemSerializer(
    BaseItemTypeSerializerMixin,
    serializers.ModelSerializer
):
    is_terminal = serializers.BooleanField(
        required=False
    )

    class Meta:
        model = AlertStatusItem
        fields = [
            "id",
            "name",
            "code",
            "is_terminal",
        ]


class AlertSerializer(
    ActiveSerializerMixin,
    TimeAuditableSerializerMixin,
    serializers.ModelSerializer
):
    # -------------------------
    # Status
    # -------------------------

    status = serializers.PrimaryKeyRelatedField(
        queryset=AlertStatusItem.objects.active()
    )

    # -------------------------
    # Generic Target
    # -------------------------

    target = GenericTargetField(
        source="*",
        required=False,
        allow_null=True,
    )

    class Meta:
        model = Alert
        fields = [
            "id",

            # target
            "target",

            # content
            "status",
            "message",
            "triggered_at",

            # lifecycle
            "is_active",
            "deactivated_at",

            # audit
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "created_at",
            "updated_at",
        ]