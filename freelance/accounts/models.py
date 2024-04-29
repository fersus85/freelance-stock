from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to='accounts/%Y/%m', blank=True,
                              null=True, verbose_name='Фото')
    is_freelancer = models.BooleanField(verbose_name='Вы фрилансер?',
                                        default=False)
    experience = models.TextField(verbose_name='Опыт',
                                  max_length=200,
                                  blank=True,
                                  null=True)
