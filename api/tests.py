from django.test import TestCase
from rest_framework.test import APIClient
from selenium import webdriver


class TestView(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_view(self):
        response = self.client.get('http://127.0.0.1:8000/api/rooms')
        self.assertEquals(response.status_code, 200)

    def test_booking(self):
        response = self.client.get('http://127.0.0.1:8000/api/book')
        self.assertNotEquals(response.status_code, 200)

    def test_login(self):
        response = self.client.get('http://127.0.0.1:8000/api/login')
        self.assertNotEquals(response.status_code, 200)


class TestSelenium(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_view_page(self):
        response = webdriver.Chrome()
        response.get('http://127.0.0.1:8000/api/rooms')
        assert 'OK' in response.page_source
        assert '200' in response.page_source
        assert 'Allow' in response.page_source
        assert 'start' in response.page_source
        assert 'name' in response.page_source
        assert 'end' in response.page_source
        assert 'booked' in response.page_source
