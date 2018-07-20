from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    sex_type = (
        (0, '男'),
        (1, '女'),
        (2, '保密')
    )
    sex = models.IntegerField(choices=sex_type, default=1, verbose_name='性别')
    head_img = models.ImageField(upload_to='user/images', blank=True, verbose_name='头像')
    phone = models.CharField(max_length=12)

    class Meta(AbstractUser.Meta):
        pass

    def __str__(self):
        return self.username

    @property
    def sex_name(self):
        return self.sex_type[self.sex][1]
