from operator import mod
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db import models


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
    facilities = models.ManyToManyField(
        'Facility', blank=True, related_name='neighborhood')
    business = models.ManyToManyField(
        'Business', blank=True, related_name='neighborhood')
    posts = models.ManyToManyField('Post', blank=True, related_name='neighborhood')

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
        self.occupants = self.user.userprofile.count()
        return self.occupants


class Facility(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, default='')
    contact = models.CharField(
        max_length=50, blank=True, null=True, default='')
    email = models.CharField(max_length=80, blank=True, null=True, default='')
    picture = models.ImageField(
        upload_to='facility_images', blank=True, null=True)
    location = models.CharField(
        max_length=50, blank=True, null=True, default='')
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


# Businessess model
class Business(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='business')
    name = models.CharField(max_length=100, blank=True, null=True, default='')
    email = models.CharField(max_length=80, blank=True, null=True, default='')
    picture = models.ImageField(
        upload_to='business', blank=True, null=True)
    location = models.CharField(
        max_length=50, blank=True, null=True, default='')
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    title = models.CharField(max_length=100, blank=True, null=True, default='')
    body = models.TextField(blank=True, null=True, default='')
    picture = models.ImageField(upload_to='post_images', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    