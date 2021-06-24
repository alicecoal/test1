from datetime import datetime

from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField

from ZZShop import settings


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150)
    age = models.IntegerField(default=18)
    level = models.IntegerField(default=0)
    country = CountryField(max_length=2, default="BY")
    signup_confirmation = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    last_login = models.DateTimeField(default=datetime.now, blank=True)

    USERNAME_FIELD = 'user'
    REQUIRED_FIELDS = ('email',)
    SOCIAL_AUTH_USER_FIELDS = ['username', 'email', 'role']

    def __str__(self):
        return self.user.username

    def object(self):
        return self

    def get_profile(self):
        return self


@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
