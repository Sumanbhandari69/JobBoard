from django.contrib import admin
from jobs.models import JobInformation, UserProfile

class JobInfo(admin.ModelAdmin):
    list_display = ("job_title", "company_name", "location", "job_description", "date_posted", "posted_by")
    list_filter = ("job_title",)
    search_fields = ("job_title", "company_name")
    date_hierarchy = "date_posted"
    ordering = ("date_posted",)
    readonly_fields = ("date_posted","posted_by") 

class UserInfo(admin.ModelAdmin):
    list_display = ("user", "full_name", "gender", "bio", "phone", "location", "education", "experience", "skills", "contact_email", "linkedin_url","github_url")
    list_filter = ("phone",)
    search_fields = ("phone", "full_name")
    ordering = ("full_name",)
    

# Register your models here.
admin.site.register(JobInformation, JobInfo)
admin.site.register(UserProfile, UserInfo)
