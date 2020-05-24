from django.test import TestCase
from .models import BucketList
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status


class ModelTestCase(TestCase):
    """This class defines the test suite for bucket list model"""

    def setUp(self):
        """Defines the test client and set up the database"""
        self.bucket_list_name = "My bucket List"
        self.bucket_list = BucketList(name=self.bucket_list_name)

    def test_model_bucket_list(self):
        """Test the bucket list model can create a bucket"""
        old_count = BucketList.objects.count()
        self.bucket_list.save()
        new_count = BucketList.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
    """Test suit for the api views"""

    def setUp(self):
        """Define the test client and other test variables"""
        self.client = APIClient()
        self.bucket_list_data = {"name": "Bike Riding"}
        self.response = self.client.post(reverse('create'), self.bucket_list_data, format="json")

    def test_api_create_bucket_list(self):
        """Test api for bucket list creation"""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
