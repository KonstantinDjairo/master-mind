from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    first_name = models.CharField(max_length=200, blank=True, default="...")
    last_name = models.CharField(max_length=200, blank=True, default="...")
    # user name do telegram como user                         
    user_name = models.CharField(max_length=255, unique=True, null=False)
    slug = models.SlugField(unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    # cliente não quer um perfil no web pro usuario
    #user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Profile') 
