"""Tests for Review Renew web application."""


from django.test import TestCase
from django.test import Client


class TestHomeView(TestCase):
    """Class containing home view tests."""

    def setUp(self):
        """Set up for client creation."""
        self.client = Client()

    def test_home_view_get_req_return_200_ok_res(self):
        """Test that a GET request to the home view returns a 200 OK HTTP
        response."""

        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)

    def test_home_view_page_named_index(self):
        """Test that the template used to render the home page is called
        index.html."""

        response = self.client.get('/')

        self.assertEqual(response.templates[0].name, 'website/index.html')
