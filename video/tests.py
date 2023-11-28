from django.test import TestCase
from django.urls import reverse_lazy
from .models import Video
from .factories import VideoFactory

# Create your tests here.
class TestVideoDetail(TestCase):
    def test_one_video_page_should_success(self):
        video_object = Video.objects.create(
            file_path="/static/video/test_video.mp4",
            name="test video 1"
        )
        response = self.client.get(f'/video/{video_object.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, video_object.name)

    def test_one_video_via_factory_boy(self):
        video_object = VideoFactory()
        response = self.client.get(f'/video/{video_object.id}/')
        # print(video_object.name)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, video_object.name)


class TestVideoList(TestCase):
    def test_video_list_should_success(self):
        for i in range(3):
            VideoFactory(name=f"test video number {i}")
        response = self.client.get(reverse_lazy('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test video number 0")
        self.assertContains(response, "test video number 1")
        self.assertContains(response, "test video number 2")
