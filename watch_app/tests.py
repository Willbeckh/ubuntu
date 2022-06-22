from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User
import unittest


# Create your tests here.
from watch_app.models import *


# models test
class TestUserModel(TestCase):
    """This class tests the user model"""

    def setUp(self):
        self.new_user = User(
            username='admin', email='admin@test.dev', password='pass12')
        self.new_user.save()

    def tearDown(self):
        User.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_user, User))

    def test_user_save(self):
        self.new_user.save()
        users = User.objects.all()
        self.assertTrue(len(users) > 0)


class TestUserProfile(TestCase):
    def setUp(self):
        user = User(
            username='admin', email='admin@test.dev', password='pass12')
        self.new_profile = UserProfile(user=user, photo='default.png', bio='test bio', phone='1111')
        
    def tearDown(self):
        UserProfile.objects.all().delete()
        
    def test_isinstance(self):
        self.assertTrue(isinstance(self.new_profile, UserProfile))
        
    
# class TestNeighborhood(self):
    