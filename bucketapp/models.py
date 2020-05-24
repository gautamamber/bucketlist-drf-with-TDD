from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.dispatch import receiver


class BucketList(models.Model):
    """Create Bucket List Model"""
    name = models.CharField(max_length=200, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="bucketlists", null=True)

    def __str__(self):
        """String representation of model object"""
        return "{}-{}".format(self.name, self.owner)

    class Meta:
        """Verbose name and verbose name plural"""
        verbose_name = "Bucket List"
        verbose_name_plural = "Bucket List"


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """Create auth token"""
    if created:
        Token.objects.create(user=instance)
