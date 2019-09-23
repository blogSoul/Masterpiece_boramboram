from django.contrib import admin
from .models import Photo

# admin.site.register(Photo)

# boraming  / aa1234

class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'author', 'created']
    raw_id_fields=['author']
    list_filter=['created',  'author']
    search_fields=['title', 'text']
    ordering = ['created']

admin.site.register(Photo, PhotoAdmin)