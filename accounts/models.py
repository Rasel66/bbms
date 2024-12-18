from django.db import models

#Create your models here.

GENDER_CHOICES = [
    ('', "--SELECT--"),
    ('male', "Male"),
    ('female', "Female"),
    ('others', "Others")
]

BLOOD_GROUP_CHOICES = [
    ('', '--SELECT--'),
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
]

class BecomeDonor(models.Model):
    name = models.CharField(max_length=100)
    phn_no = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    blood_group = models.CharField(max_length=10, choices=BLOOD_GROUP_CHOICES)
    address = models.TextField()

    def __str__(self):
        return f'{self.name} ({self.blood_group})'