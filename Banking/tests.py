from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client

from django.urls import reverse


class TestUrl(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_login_url(self):
        url = reverse("Banking:login")
        get_response = self.client.get(url)
        post_response = self.client.post(url)
        self.assertEqual(get_response.status_code, 405)
        self.assertEqual(post_response.status_code, 200)

    def test_all_users_url(self):
        url = reverse("Banking:all_users")
        get_response = self.client.get(url)
        post_response = self.client.get(url)
        self.assertEqual(get_response.status_code, 200)
        self.assertEqual(post_response.status_code, 200)



