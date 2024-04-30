from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    photo = models.ImageField(upload_to='accounts/%Y/%m', blank=True,
                              null=True, verbose_name='Фото')
    is_freelancer = models.BooleanField(verbose_name='Вы фрилансер?',
                                        default=False)
    experience = models.TextField(verbose_name='Опыт',
                                  max_length=200,
                                  blank=True,
                                  null=True)
