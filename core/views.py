from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from video.models import Video
from .models import Profile
from .forms import ProfileForm

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

def profile_create(request):
    context = {}
    if request.method == "POST":
        profile_form = ProfileForm(
            data=request.POST,
            files=request.FILES
        )
        if profile_form.is_valid():
            profile_object = profile_form.save(commit=False)
            profile_object.user = request.user
            profile_object.save()
            messages.success(request, "Профиль и канал успешно созданы")
            return redirect(f'/profile/{profile_object.id}/')
        else:
            messages.error(request, "Ошибка при создании профиля")

    profile_form = ProfileForm()
    context["profile_form"] = profile_form
    return render(
        request=request,
        template_name="profile_create.html",
        context=context
    )

def profile_detail(request, id):
    profile_object = Profile.objects.get(id=id)
    return render(
        request,
        'profile.html',
        {"profile_object": profile_object}
    )

def profile_update(request, id):
    context = {}
    profile_object = Profile.objects.get(id=id)
    if request.user == profile_object.user:
        if request.method == "POST":
            profile_form = ProfileForm(
                instance=profile_object,
                data=request.POST,
                files=request.FILES,
            )
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, "Профиль успешно обновлён!")
                return redirect(profile_detail, id=profile_object.id)

        profile_form = ProfileForm(instance=profile_object)
        context["profile_form"] = profile_form
        return render(request, "profile_update.html", context)
    else:
        return HttpResponse("Нет доступа")

def profile_delete(request, id):
    profile_object = Profile.objects.get(id=id)
    if request.user == profile_object.user:
        context = {"profile_object": profile_object}
        if request.method == "POST":
            profile_object.delete()
            return redirect(homepage)
        return render(request, "profile_delete.html", context)
    else:
        return HttpResponse("Нет доступа")