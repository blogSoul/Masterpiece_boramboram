from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
#from django.conf import settings  # 이게필요한가

'''
# def자료
#https://wayhome25.github.io/django/2017/03/14/django-07-kilogram-04-photo-model/
def user_path(instance, filename): #파라미터 instace는 Photo모델을 의미. filenema은 업로드 된 파일의 파일이름
    ext = filename.split('.')[-1]
    if instance.pk:
        return '{}.{}'.format(instance.pk, ext)
    else:
        pass
'''

class Photo(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_photos') 
    category= models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/', default = 'photos/no_image.png') # upload 된 장소 글쓴이 폴더에 가는거 이상??????? 
    text=models.TextField()
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']     # 업로드내림차순으로 정렬


    def __str__(self): 
        return self.author.username + " " + self.created.strftime("%Y-%m-%d %H:%M:%S")

    def get_absolute_url(self):
        return reverse('Mainscreen:detail', args=[str(self.id)])
        # 상세 페이지 주소 반환              # args : 여러값을 리스트로 전달-> URL만드는데 필요한 pk값 전달
        # reverse 메소드 : URL 패턴 이름을 가지고 해당 패턴을 찾아 주소를 만들어주는 함수.

