from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='user')
    photo = models.ImageField(
        upload_to='profile_images', blank=True, null=True)
    bio = models.TextField(blank=True, default='', null=True, max_length=500)
    phone = models.CharField(max_length=20, blank=True, null=True, default='')
    # neighborhood = models.CharField(max_length=50, blank=True, null=True, default='')
    block = models.CharField(max_length=80, blank=True, null=True, default='')

    def create_profile(sender, **kwargs):
        user = kwargs['instance']
        if kwargs['created']:
            user_profile = UserProfile(user=user)
            user_profile.save()
    post_save.connect(create_profile, sender=User)
