from django.shortcuts import render

from .models import Photo

def photo_list(request):
    photo = Photo.objects.all()
    return render(request, 'Mainscreen/home.html', {'photos':photos})
    # render : home.html 템플릿 렌더링


class PhotoUploadView(CreateView):
    model=Photo
    fields = ['photo', 'text']
    template_name = 'Mainscreen/request.html'

    # 업로드를 끝낸 후 이동할 페이지를 호출
    def form_valid(self, form):
        form.instance.author_id : self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else :
            return self.render_to_response({'form':form})


class PhotoDeleteView(DeleteView):
    model = Photo
    success_url = '/'
    template_name = '' # photo/delete.html 같은 url 입력

class PhotoUpdateView(UpdateView):
    model =Photo
    fields=['photo', 'text']
    template_name = '' #photo/update.html 같은 url입력