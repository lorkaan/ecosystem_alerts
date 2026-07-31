from django.contrib import admin

from .models import Alert, AlertStatusItem

# Register your models here.
admin.register(AlertStatusItem)
admin.register(Alert)