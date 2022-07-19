from email.policy import default
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    image = models.ImageField(
        upload_to='profile_image', default='blank-image.png')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100, null=True, blank=True)
    lastname = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
