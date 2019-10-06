from django.db import models
# Create your models here.
class Art(models.Model):
    CATEGORY = (
        ('ill', 'illustration'),
        ('cha', 'character'),
        ('por', 'portrait'),
        ('cal', 'calligraphy'),
        ('web', 'webtoon'),
        ('vid', 'video'),
        ('oth', 'other')
    )
    category = models.CharField(max_length=3, choices=CATEGORY)
    created_at_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', blank=True)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

    who_make = models.CharField(max_length=30)
    #현재 로그인되어있는 사용자의 id를 저장할 예정입니다.

    def summary(self):
        return self.body[:100]
