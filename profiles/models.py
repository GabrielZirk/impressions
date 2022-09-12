from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(blank=True, max_length=500)
    country = CountryField(blank_label='Select your country', blank=True)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(
        default="default_avatar.jpg", upload_to="profile_images")

    def __str__(self):
        return f"Username: {self.user.username}"
