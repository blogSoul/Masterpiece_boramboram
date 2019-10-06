from django.db import models
# Create your models here.
class Request(models.Model):
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
    request_at_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='request/', blank=True)
    title = models.CharField(max_length=30)
    description = models.TextField()
    how_much_request = models.IntegerField()
    when_end = models.DateField()

    who_request = models.CharField(max_length=30)
    #현재 로그인되어있는 사용자의 id를 저장할 예정입니다.

    def summary(self):
        return self.body[:100]
