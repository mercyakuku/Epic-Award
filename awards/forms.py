from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        user.save()

        return user

class WebsitePostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('name', 'landing_image',
                  'screenshot_1', 'screenshot_2', 'screenshot_3', 'screenshot_4', 'description', 'site_link', 'country')        

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        exclude = ['user', 'post', 'state', 'zipcode', 'address']                  

class AddressForm(forms.ModelForm):
    class Meta:
        model = Location
        exclude = ['user', 'post']  


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'is_judge', 'is_pro',
                   'is_chief', 'is_tribe', 'user_address']
        list_display = []              