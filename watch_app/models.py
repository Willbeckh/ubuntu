import email
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='user')
    photo = models.ImageField(
        upload_to='profile_images', blank=True, null=True, default='profile_images/default.png')
    location = models.CharField(
        max_length=100, blank=True, null=True, default='')
    bio = models.TextField(blank=True, default='', null=True, max_length=500)
    phone = models.CharField(max_length=20, blank=True, null=True, default='')
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    neighborhood = models.ForeignKey(
        'Neighborhood', on_delete=models.CASCADE, null=True, blank=True)
    street = models.CharField(max_length=80, blank=True, null=True, default='')

    def __str__(self):
        return self.user.username

    def create_profile(sender, **kwargs):
        user = kwargs['instance']
        if kwargs['created']:
            user_profile = UserProfile(user=user)
            user_profile.save()
    post_save.connect(create_profile, sender=User)

    # if user has photo, display it, else display default

    def image_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

# neighborhood model


class Neighborhood(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True, default='')
    location = models.CharField(
        max_length=50, blank=True, null=True, default='')
    occupants = models.IntegerField(blank=True, null=True, default=0)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='neighborhood', blank=True, null=True)
    # business = models.ForeignKey('Business', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    def create_neighborhood(self):
        return self.save()

    def update_neighborhood(self):
        pass

    def delete_neighborhood(self):
        pass

    def find_neighborhood_by_id(self, id):
        pass

    def update_occupants(self):
        pass

    def count_occupants(self):
        pass


class Facility(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, default='')
    contact = models.CharField(
        max_length=50, blank=True, null=True, default='')
    email = models.CharField(max_length=80, blank=True, null=True, default='')
    picture = models.ImageField(
        upload_to='facility_images', blank=True, null=True)
    location = models.CharField(
        max_length=50, blank=True, null=True, default='')
    neighborhood = models.ManyToManyField(
        Neighborhood, related_name='facilities', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name