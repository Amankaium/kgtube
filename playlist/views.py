from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import UserPlayList
from .forms import PlayListForm

# Create your views here.
def playlists(request):
    query_result = UserPlayList.objects.all()
    context = {"objects_list": query_result}
    return render(
        request,
        'playlists.html',
        context
    )


class PlayListView(ListView):
    model = UserPlayList


def playlist_info(request, id):
    playlist_object = UserPlayList.objects.get(id=id)
    context = {"playlist_object": playlist_object}
    return render(request, "playlist_info.html", context)



def playlist_add(request):
    if request.method == "POST":
        # request.POST - это словарь
        name = request.POST["playlist_name"] # str 
        description = request.POST["description"] # str
        # print(request.POST)
        # print(name)
        # INSERT INTO UserPlayList ...
        playlist_object = UserPlayList.objects.create(
            name=name,
            description=description,
        )
        return redirect(playlist_info, id=playlist_object.id)
    
    return render(request, "playlist_add.html")

def playlist_df_add(request):
    context = {}
    if request.method == "POST":
        # код создания playlist 

        # создаём объект формы с значениями
        playlist_form = PlayListForm(request.POST)
        # проверка валидности
        if playlist_form.is_valid():
            # создаём запись в БД
            playlist_object = playlist_form.save()
            return redirect(playlist_info, id=playlist_object.id)
    
    playlist_form = PlayListForm()
    context["playlist_form"] = playlist_form
    return render(request, "playlist_df_add.html", context)
