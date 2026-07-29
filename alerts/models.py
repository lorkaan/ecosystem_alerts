from django.db import models
from django.utils import timezone
import pghistory

from foundations.ecosystem_foundations.base.models import BaseItemType, OptionalGenericUuidTargetMixin, BaseUuidPrimaryKeyModel

# Create your models here.
class AlertStatusItem(BaseItemType):
    is_terminal = models.BooleanField(default=False)

    def __str__(self):
        return self.name

@pghistory.track()
class Alert(OptionalGenericUuidTargetMixin, BaseUuidPrimaryKeyModel):
    status = models.ForeignKey(AlertStatusItem, on_delete=models.PROTECT)
    message = models.TextField()
    triggered_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["triggered_at"]