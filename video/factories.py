import factory
from django.contrib.auth.models import User
from .models import Video


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username',)

    username = 'test_user_1'


class VideoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Video
    
    file_path = factory.django.FileField(file_path="/static/video/test_video.mp4") 
    name = factory.Sequence(lambda n: f"Test video {n}")
    author = factory.SubFactory(UserFactory)
