from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class myuser(AbstractUser):
    user_realname = models.CharField(max_length=15)
    user_phone_number = models.CharField(max_length=15)
    isdesigner = models.BooleanField(default=False)
    is_art = models.BooleanField(default=False)
#나중에 추가하기
#프로필 사진은 form형식으로 지정해야 해서 추가사항으로 남겨주겠습니다.
#Art 부분은 조금 더 논의하고 만들겠습니다.

