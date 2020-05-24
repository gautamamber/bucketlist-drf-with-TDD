from rest_framework import generics
from .serializers import BucketListSerializer
from . import models


class CreateView(generics.ListCreateAPIView):
    """This class defines the create and list of bucket"""
    queryset = models.BucketList.objects.all()
    serializer_class = BucketListSerializer

    def perform_create(self, serializer):
        """Save the post data"""
        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class Handles GET, PUT, DELETE api"""
    queryset = models.BucketList.objects.all()
    serializer_class = BucketListSerializer

