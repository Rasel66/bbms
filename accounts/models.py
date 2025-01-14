from django.db import models
from django.contrib.auth.models import AbstractUser
from .choices import GENDER_CHOICES, BLOOD_GROUP_CHOICES, USER_TYPES

#Create your models here.

class CustomUser(AbstractUser):
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='donor')

    def __str__(self):
        return f"{self.user_type}"

class Donor(models.Model):
    name = models.CharField(max_length=100)
    phn_no = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    blood_group = models.CharField(max_length=10, choices=BLOOD_GROUP_CHOICES)
    address = models.TextField()

    def __str__(self):
        return f'{self.name} ({self.blood_group})'