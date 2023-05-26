import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.UUIDField(
        'Уникальный UUID',
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )
