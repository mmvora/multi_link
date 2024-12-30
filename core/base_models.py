import uuid
from django.db import models


class BaseModel(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, primary_key=True, auto_created=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True
