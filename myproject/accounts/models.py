from django.db import models
from django.core.validators import RegexValidator
from django.core.mail import send_mail

# Create your models here.
class webuser(models.Model):
    user_id = models.CharField(max_length=15)
    user_pw = models.CharField(max_length=15)
    user_nk = models.CharField(max_length=15)
    user_em = models.CharField(max_length=20)

    user_ph1 = models.CharField(max_length=3)
    user_ph2 = models.CharField(max_length=4)
    user_ph3 = models.CharField(max_length=4)

class PhoneModel(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}9$', message = "Phone number must be entered in the format: '+999999999', Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], blank=True) # validators should be a list
# 전화번호 저장을 확인하는 부분!
