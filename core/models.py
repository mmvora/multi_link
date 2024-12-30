from django.db import models
from datetime import datetime

from core.base_models import BaseModel
from users.models import CustomUser


class Link(BaseModel):
    created_by = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="links"
    )
    url = models.URLField()
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(
        "UserLinkCategory",
        on_delete=models.CASCADE,
        related_name="links",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.deleted_at = datetime.now()
        self.save()


class UserLinkCategory(BaseModel):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="categories"
    )
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"
