from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    is_freelancer = models.BooleanField(verbose_name='Вы фрилансер?',
                                        default=False)
    experience = models.TextField(verbose_name='Опыт',
                                  max_length=200,
                                  blank=True,
                                  null=True)
