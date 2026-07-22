from base.registry import SIGNAL_REGISTRY
from .signals import CREATE_ALERT
from .models import Alert, AlertStatus

@SIGNAL_REGISTRY.register(CREATE_ALERT)
def create_alert_handler(payload, **kwargs):
    """
    payload example:
    {
        "reason": <AlertReason>,
        "severity": <AlertSeverity>,
        "target": <model instance>,
        "message": "Something happened"
    }
    """

    target = payload.get("target")

    alert = Alert(
        reason=payload["reason"],
        severity=payload["severity"],
        status=AlertStatus.objects.get(code="open"),
        message=payload.get("message", ""),
    )

    if target:
        alert.set_target(target)

    alert.save()

    return alert