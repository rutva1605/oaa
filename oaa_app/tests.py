from django.test import TestCase, Client
from django.urls import reverse, resolve
from .views import home_view, data_view, data_visualization_view
from django.db import connection

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_view(self):
        response = self.client.get(reverse('oaa_app:home'))  
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'oaa_app/home.html')
        print("Home view test successful!")

    def test_data_view(self):
        response = self.client.get(reverse('oaa_app:data'))  
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'oaa_app/data.html')
        print("Data view test successful!")

    def test_data_visualization_view(self):
        response = self.client.get(reverse('oaa_app:data visualization'))  
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'oaa_app/data_visualization.html')
        print("Data visualization view test successful!")

    def test_home_url_resolves(self):
        url = reverse('oaa_app:home')
        self.assertEqual(resolve(url).func, home_view)
        print("Home URL resolves test successful!")

    def test_data_url_resolves(self):
        url = reverse('oaa_app:data')
        self.assertEqual(resolve(url).func, data_view)
        print("Data URL resolves test successful!")

    def test_data_visualization_url_resolves(self):
        url = reverse('oaa_app:data visualization')
        self.assertEqual(resolve(url).func, data_visualization_view)
        print("Data visualization URL resolves test successful!")

class DatabaseConnectionTestCase(TestCase):
    def test_database_connection(self):
        # Try to establish a connection with the database
        try:
            connection.ensure_connection()
            connected = True
            print("Successfully connected to the database!")
        except Exception as e:
            connected = False
            print(f"Failed to connect to the database: {e}")

        # Assert that the connection was successful
        self.assertTrue(connected, "Failed to connect to the database")
