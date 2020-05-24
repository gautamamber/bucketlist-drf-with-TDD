from django.test import TestCase
from .models import BucketList
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User


class ModelTestCase(TestCase):
    """This class defines the test suite for bucket list model"""

    def setUp(self):
        """Defines the test client and set up the database"""
        user = User.objects.create(username="amber gautam")
        self.bucket_list_name = "My bucket List"
        self.bucket_list = BucketList(name=self.bucket_list_name, owner=user)

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
        user = User.objects.create(username="amber gautam")
        self.client = APIClient()
        self.bucket_list_data = {"name": "Bike Riding", "owner": user.id}
        self.response = self.client.post(reverse('create'), self.bucket_list_data, format="json")

    def test_api_create_bucket_list(self):
        """Test api for bucket list creation"""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_get_bucket_list(self):
        """Test the api can get a given a bucket list"""
        bucket_list = BucketList.objects.get()
        response = self.client.get(reverse('details-bucket', kwargs={
            'pk': bucket_list.id
        }), format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, bucket_list)

    def test_api_update_bucket_list(self):
        """Test api for bucket update"""
        bucket_list = BucketList.objects.get()
        change_bucket = {"name": "Bike ride"}
        res = self.client.put(
            reverse("details-bucket", kwargs={"pk": bucket_list.id}
        ), change_bucket, format="json")
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_delete_bucket_list(self):
        """Test api for delete bucket list"""
        bucket_list = BucketList.objects.get()
        response = self.client.delete(
            reverse("details-bucket", kwargs={"pk": bucket_list.id}),
            format="json", follow=True
        )
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
