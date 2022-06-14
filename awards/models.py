from django.db import models
from django.contrib.auth.models import User
import math

# Create your models here.
class Location(models.Model):
    country = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    zipcode = models.IntegerField(null=True)
    address = models.IntegerField(null=True)

    def __str__(self):
        return self.country

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, related_name='profile')
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    profile_photo = models.ImageField(upload_to='images/', blank=True,default='dwf_profile.jpg')
    user_name = models.CharField(max_length=50, null=True)
    occupation = models.CharField(max_length=300, null=True)
    company_name = models.CharField(max_length=300, null=True)
    bio = models.TextField(blank=True)
    website = models.CharField(max_length=150, null=True)
    facebook = models.CharField(max_length=200, null=True)
    twitter = models.CharField(max_length=200, null=True)
    instagram = models.CharField(max_length=200, null=True)
    linkedin = models.CharField(max_length=200, null=True)
    STATUS_CHOICES = (
        ('Male', ("Male")),
        ('Female', ("Female")),
        ('Other', ("Other")),
    )
    gender = models.CharField(
        max_length=20, choices=STATUS_CHOICES, blank=True)
    age = models.IntegerField(blank=True, null=True)
    phone = models.IntegerField(null=True)
    email = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    zipcode = models.IntegerField(null=True)
    address = models.IntegerField(null=True)
    is_judge = models.BooleanField(default=False)
    is_pro = models.BooleanField(default=False)
    is_chief = models.BooleanField(default=False)
    is_tribe = models.BooleanField(default=False)

    def save_profile(self, current_user):
        self.is_chief = False
        self.is_pro = False
        self.is_judge = False
        self.is_tribe = False
        self.user = current_user
        self.save()

    def __str__(self):
        return self.user_name        
