from django.shortcuts import render, HttpResponse
from video.models import Video
from .models import Profile

# Create your views here.
def homepage(request):
    # return HttpResponse("hello world")
    return render(request, "home.html")

def about_view(request):
    return render(request, 'about.html')

def search(request):
    key_word = request.GET["key_word"]
    # SELECT * FROM Video WHERE name LIKE '%key_word%'
    videos_query = Video.objects.filter(name__contains=key_word)
    context = {"videos_list": videos_query}
    return render(request, "videos.html", context)

def profile_detail(request, id):
    profile_object = Profile.objects.get(id=id)
    return render(
        request,
        'profile.html',
        {"profile_object": profile_object}
    )
