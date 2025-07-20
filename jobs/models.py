from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class JobInformation(models.Model):
    job_title = models.CharField(max_length=30)
    company_name = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
    job_description = models.CharField(blank=True, default="")
    date_posted = models.DateField(auto_now=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        ('N', 'Prefer not to say'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    bio = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100, blank=True)
    education = models.TextField(blank=True)
    experience = models.TextField(blank=True)
    skills = models.TextField(blank=True)
    contact_email = models.EmailField(blank=True)
    linkedin_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"