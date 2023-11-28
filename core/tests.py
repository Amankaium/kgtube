from django.test import TestCase
from django.urls import reverse_lazy


class TestHomepage(TestCase):
    def test_open_homepage_should_success(self):
        response = self.client.get(reverse_lazy("home"))
        # assert response.status_code == 200
        self.assertEqual(response.status_code, 200)


class TestAboutPage(TestCase):
    def test_open_about_page_should_success(self):
        response = self.client.get("/about/")
        assert response.status_code == 200
