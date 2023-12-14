import uuid

from django.core.validators import FileExtensionValidator
from django.db import models

from users.models import User


class Audiorecord(models.Model):
    id = models.UUIDField(
        'Уникальный UUID',
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='author',
        verbose_name='Автор',
    )
    audio = models.FileField(
        'Аудиофайл',
        upload_to='',
        validators=[FileExtensionValidator(allowed_extensions=['wav'])]
    )
