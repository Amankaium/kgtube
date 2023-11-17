"""
URL configuration for kgtube project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import homepage, about_view, search
from playlist.views import playlists, playlist_add, playlist_info
# from playlist import views
from video.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('about/', about_view),
    path('playlists/', playlists),
    # path('playlists/', views.playlists),
    path('playlist/<int:id>/', playlist_info, name='playlist-info'),
    path('playlist/add/', playlist_add, name='playlist-add'),
    path('videos/', videos),
    path('video/<int:id>/', video),
    path('video-update/<int:id>/', video_update, name='video-update'),
    path('video-delete/<int:id>/', video_delete, name='video-delete'),
    path('video-add/', video_add, name='video-add'),
    path('search/', search, name='search'), # from core.views import search
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
