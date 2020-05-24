from rest_framework import serializers
from . import models


class BucketListSerializer(serializers.ModelSerializer):
    """Serializer to map the model instance into JSON"""

    class Meta:
        model = models.BucketList
        fields = "__all__"
