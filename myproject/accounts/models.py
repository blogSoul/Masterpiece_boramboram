from django.db import models

# Create your models here.
class webuser(models.Model):
    user_id = models.CharField(max_length=15)
    user_pw = models.CharField(max_length=15)
    user_nk = models.CharField(max_length=15)
    user_em = models.CharField(max_length=20)

    user_ph1 = models.CharField(max_length=3)
    user_ph2 = models.CharField(max_length=4)
    user_ph3 = models.CharField(max_length=4)