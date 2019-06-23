from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from hackerhub.models import Hackathon
from phone_field import PhoneField
# from django import forms

# Create your models here.

# User comes with: first name, last name, email

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # ===== social media links =====

    github = models.CharField(max_length=30, null=True, blank=True)

    devpost = models.CharField(max_length=30, null=True, blank=True)

    linkedin = models.CharField(max_length=30, null=True, blank=True)

    # ===== tags =====

    TAGS = [
        ('New', 'New hacker'),
        ('Developer', 'Developer'),
        ('Business', 'Business'),
        ('Designer', 'Designer'),
    ]

    phone = models.CharField(max_length=10, blank=True, default='')

    skillset = models.CharField(max_length=200, blank=True, default='')

    tags = models.CharField(max_length=15, default='New', choices=TAGS)

    bio = models.TextField(max_length=900, blank=True, default='')

    # prevHackathons = models.ManyToManyField(Hackathon)

    def __str__(self):
        return self.user.username





# signal - every time a new User account is created, a corresponding Profile
#    is created as well
def create_profile(sender, **kwargs):
    if kwargs['created']:
        profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)


