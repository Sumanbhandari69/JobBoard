from django.contrib import admin
from jobs.models import JobInformation

class JobInfo(admin.ModelAdmin):
    list_display = ("job_title", "company_name", "location", "job_description", "date_posted")
    list_filter = ("job_title",)
    search_fields = ("job_title", "company_name")
    date_hierarchy = "date_posted"
    ordering = ("date_posted",)
    readonly_fields = ("date_posted",) 

# Register your models here.
admin.site.register(JobInformation, JobInfo)
