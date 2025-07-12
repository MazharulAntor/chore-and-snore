from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    OCCUPATION_CHOICES = (
        ('student', 'Student'),
        ('labor', 'Labor'),
        ('job_holder', 'Job Holder'),
        ('freelancer', 'Freelancer'),
        ('unemployed', 'Unemployed'),
        ('other', 'Other'),
    )
    occupation = models.CharField(max_length=20, choices=OCCUPATION_CHOICES, default='student')
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.username
