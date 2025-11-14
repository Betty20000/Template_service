from django.db import models
import uuid
from django.utils import timezone


class Template(models.Model):
    template_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255)
    version = models.CharField(max_length=10, default="latest")
    language = models.CharField(max_length=2, default="en")
    type = models.CharField(max_length=10)
    subject = models.TextField(blank=True, null=True)

    body = models.JSONField(default=dict)
    variables = models.JSONField(default=list)
    metadata = models.JSONField(default=dict)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ("name", "language", "version")

    def __str__(self):
        return f"{self.name} ({self.language}) v{self.version}"

    def save(self, *args, **kwargs):
        # Automatically truncate all CharFields to their max_length
        for field in self._meta.fields:
            if isinstance(field, models.CharField):
                value = getattr(self, field.name)
                if value and field.max_length:
                    setattr(self, field.name, value[:field.max_length])
        super().save(*args, **kwargs)
