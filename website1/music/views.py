from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse, request, response, Http404
from website1.music.models import Album, Song
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate,login
from django.views.generic import View
from music import Userform


'''def index(request):
    details = Album.objects.all()
    context = {'details': details}
    return render(request, 'music/index.html', context)'''

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    def get_queryset(self):
        return Album.objects.all()


def details(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album':album})

def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except(KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {

            'album':album,
            'error_message':'you did something wrong',
        })
    else:
        selected_song.stared = True
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album})



class AlbumCreate(generic.CreateView):
    model = Album
    fields = {'artist', 'genre', 'album_title', 'logo'}

class Albumupdate(generic.UpdateView):
    model = Album
    fields = {'artist', 'genre', 'album_title', 'logo'}

class AlbumDelete(generic.DeleteView):
    model = Album
    success_url = reverse_lazy('index')

class UserFormView(View):
    form_class = Userform
    template_name = 'music/registration.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})


    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            # normalize

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user.set_password(password)
            user.save()

            # return user objects if fields are correct

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:

                    login(request, user)
                    request.user
                    return redirect('index')

        return render(request, self.template_name, {'form': form})
