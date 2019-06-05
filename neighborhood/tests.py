from django.test import TestCase
from django.test import TestCase
from django.contrib.auth.models import User
from .models import *




class UserTest(TestCase):
    def setUp(self):
        self.user=User(username='Emma',first_name='Emma',last_name='Kibore',email='emmaKibore@gmail.com')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.user,User))
    
    def test_data(self):
        self.assertTrue(self.user.username,'Emma')
        self.assertTrue(self.user.first_name,'Emma')
        self.assertTrue(self.user.last_name,'Emma')
        self.assertTrue(self.user.email,'emmaKibore@gmail.com')
    
    def test_save(self):
        self.user.save()
        users = User.objects.all()
        self.assertTrue(len(users)>0)
    
    def test_delete(self):
        user = User.objects.filter(id=1)
        user.delete()
        users = User.objects.all()
        self.assertTrue(len(users)==0)


