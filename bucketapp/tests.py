from django.test import TestCase
from .models import BucketList


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
