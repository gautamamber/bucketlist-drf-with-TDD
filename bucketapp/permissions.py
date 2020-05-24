from rest_framework.permissions import BasePermission
from . import models


class IsOwner(BasePermission):
    """Custom permission"""

    def has_object_permission(self, request, view, obj):
        """Return True is permission is granted to owner"""
        if isinstance(obj, models.BucketList):
            return obj.owner == request.user
        return obj.owner == request.user
