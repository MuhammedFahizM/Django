from django.test import TestCase

# Create your tests here.

from rest_framework.test import APITestCase

class TaskAPITestCase(APITestCase):
    def test_get_tasks(self):
        response = self.client.get('generic_view/')
        self.assertEqual(response.status_code,200)

