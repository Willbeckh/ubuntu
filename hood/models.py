from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from datetime import datetime as dt

from django.db.models.signals import post_save







# Create your models here.





class Location(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)


    #save location

    def save_location(self):
        self.save()

    def __str__(self):
        return self.name





class NeighbourHood(models.Model):
    name = models.CharField(max_length=255)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    occuppants_count = models.IntegerField(default=0)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profile', default="avatar.png")
    bio = models.TextField(null=True, blank=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    location = models.ForeignKey(Location, null="false" ,on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(NeighbourHood, null="false", on_delete=models.CASCADE)
   


    def create_profile(sender, **kwargs):



        user = kwargs["instance"]

        if kwargs["created"]:


            user_profile = Profile(user=user)
            user_profile.save()

    post_save.connect(create_profile, sender=User)



    def __str__(self):
        return self.user.username



class Business(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
 
 


    def __str__(self):
        return self.name

class  Contact(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50 , blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)



    def __str__(self):


        return self.name


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="post-images", null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE , default=1)
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.title