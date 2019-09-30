from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class myuser(AbstractUser):
    user_name = models.CharField(max_length=15)
    user_password = models.CharField(max_length=15)
    user_nickname = models.CharField(max_length=15)
    user_email = models.CharField(max_length=20)
    user_phone_number = models.CharField(max_length=15)

#Art 부분은 조금 더 논의하고 만들겠습니다.
