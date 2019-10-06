from django.contrib import admin
from .models import Art
# Register your models here.
@admin.register(Art)
class ArtAdmin(admin.ModelAdmin):
    list_display = ['title','category','created_at_time','who_make','description','who_make']


#admin 페이지가 보이지 않는 경우가 생긴다.
#category가 문제인데 조금만 쉬고 다시 생각해보자
#잠시 개발을 위해 category 부분 생략!