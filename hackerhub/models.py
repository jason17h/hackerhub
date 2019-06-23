from django.db import models
from accounts.models import User

# Create your models here.

class Hackathon(models.Model):

    name = models.CharField(max_length=50, blank=True, default='')

    eventId = models.CharField(max_length=50, blank=True, default='')

    startDate = models.DateField(null=True)
    endDate = models.DateField(null=True)

    location = models.TextField(max_length=100, blank=True, default='')

    description = models.TextField(max_length=800, blank=True, default='')

    participants = models.ManyToManyField(User, blank=True)

    website = models.URLField(null=True, blank=True)

    logo = models.ImageField(upload_to='hackathon_pics', null=True)

    # winners = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.name

class Team(models.Model):
    
    teamName = models.CharField(max_length=50, blank=True, default='')

    hackathon = models.ForeignKey('Hackathon', on_delete=models.CASCADE)

    # creator = models.ForeignKey(User, on_delete=models.CASCADE)
    
    members = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.teamName

