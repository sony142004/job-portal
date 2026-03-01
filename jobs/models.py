from django.db import models
from django.utils import timezone

class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    job_type = models.CharField(max_length=50)
    work_setup = models.CharField(max_length=50) 
    level = models.CharField(max_length=50, blank=True) 
    salary_range = models.CharField(max_length=100) 
    company_size = models.CharField(max_length=100, blank=True)
    industry = models.CharField(max_length=200, blank=True) 
    skills = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)
    role_description = models.TextField(blank=True)
    posted_date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    logo_color = models.CharField(max_length=50, default="#000000") 

    def __str__(self):
        return f"{self.title} at {self.company}"
