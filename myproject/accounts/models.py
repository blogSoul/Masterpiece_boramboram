from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class myuser(AbstractUser):
    user_realname = models.CharField(max_length=15)
    user_phone_number = models.CharField(max_length=15)
    isdesigner = models.BooleanField(default=False)
#Art 부분은 조금 더 논의하고 만들겠습니다.
