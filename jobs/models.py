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

