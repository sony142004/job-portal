from django.contrib import admin
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'posted_date', 'is_active')
    list_filter = ('job_type', 'work_setup', 'level', 'is_active')
    search_fields = ('title', 'company', 'location', 'skills')
