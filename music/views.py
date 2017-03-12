from django.views import generic
from django.http import HttpResponse
from . models import  Album, Song
from django.shortcuts import render, get_object_or_404

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'
    def get_queryset(self):
        return Album.objects.all()



class DetailsView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'

'''
def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums}
    return render(request,'music/index.html', context)


def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request,'music/detail.html', {'album': album})
'''