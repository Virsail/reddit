from django.db import models
from pyuploadcare.dj.models import ImageField
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models import ObjectDoesNotExist



# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    picture = models.ImageField(upload_to = 'profile_pics/', blank=True, default='profile_pics/default.jpg')

