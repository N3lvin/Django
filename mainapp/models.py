from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
       
        image=models.ImageField()

class Songs(models.Model):
        name=models.CharField(max_length=20)
        artist=models.CharField(max_length=32)
        listeners=models.IntegerField()
        lyrics=models.TextField()

class Teamresults(models.Model):
        Team=models.CharField(max_length=20)
        numberofwins=models.CharField(max_length=40)   
        numberofdraws=models.CharField(max_length=40)   

