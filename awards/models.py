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

class Post(models.Model):
    uploaded_by = models.ForeignKey(User, null=True, related_name='posts')
    country = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=200, null=True)
    landing_image = models.ImageField(upload_to='site-images/', null=True)
    screenshot_1 = models.ImageField(upload_to='site-images/', null=True)
    screenshot_2 = models.ImageField(upload_to='site-images/', null=True)
    screenshot_3 = models.ImageField(upload_to='site-images/', null=True)
    screenshot_4 = models.ImageField(upload_to='site-images/', null=True)
    description = models.TextField(blank=True)
    site_link = models.CharField(max_length=200, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    is_sotd = models.BooleanField(default=False)
    is_hm = models.BooleanField(default=False)
    is_soty = models.BooleanField(default=False)
    is_mow = models.BooleanField(default=False)
    is_ds = models.BooleanField(default=False)

    @classmethod
    def all_posts(cls):
        all_posts = cls.objects.all()
        return all_posts

    @classmethod
    def filter_by_search_term(cls, search_term):
        return cls.objects.filter(description__icontains=search_term)

    def get_user_profile(self, post):
        posts = self.objects.filter(uploaded_by=post.uploaded_by)
        return posts

    def get_one_post(self, post_id):
        return self.objects.get(pk=post_id)

    def save_post(self, user):
        self.is_ds = False
        self.is_hm = False
        self.is_mow = False
        self.is_sotd = False
        self.is_soty = False
        self.uploaded_by = user
        self.save()

    def __str__(self):
        return self.name
