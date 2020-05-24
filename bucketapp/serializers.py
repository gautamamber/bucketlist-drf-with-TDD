from rest_framework import serializers
from . import models


class BucketListSerializer(serializers.ModelSerializer):
    """Serializer to map the model instance into JSON"""
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = models.BucketList
        fields = "__all__"
