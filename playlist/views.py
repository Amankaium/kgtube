from django.shortcuts import render, redirect
from .models import UserPlayList

# Create your views here.
def playlists(request):
    # SELECT * FROM UserPlayList;
    query_result = UserPlayList.objects.all()

    # query_result является списком 
    context = {"objects_list": query_result}

    return render(
        request,
        'playlists.html',
        context
    )

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
        playlist_object = UserPlayList.objects.create(
            name=name,
            description=description,
        )
        return redirect(playlist_info, id=playlist_object.id)
    
    return render(request, "playlist_add.html")