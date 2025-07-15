from django.db import models

# Create your models here.

class JobInformation(models.Model):
    job_title = models.CharField(max_length=30)
    company_name = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
    job_description = models.CharField(blank=True, default="")
    date_posted = models.DateField(auto_now=True)

