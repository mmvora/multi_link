from django.db import models
from core.base_models import BaseModel
from users.models import CustomUser


class Link(BaseModel):
    created_by = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="links"
    )
    url = models.URLField()
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    category = models.ForeignKey(
        "UserLinkCategory", on_delete=models.CASCADE, related_name="links", null=True
    )

    def __str__(self):
        return self.title


class UserLinkCategory(BaseModel):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="categories"
    )
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user} - {self.name}"
