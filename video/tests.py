from django.test import TestCase
from django.urls import reverse_lazy
from .models import Video

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
