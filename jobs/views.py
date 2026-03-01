from django.shortcuts import render
from .models import Job
from django.utils import timezone

def index(request):
    """
    Step 1: Fetch jobs from the SQL database using Django ORM.
    We order them by the 'posted_date' field, so newest jobs appear first.
    """
    db_jobs = list(Job.objects.all().order_by('-posted_date'))

    """
    Step 2: Define static jobs directly in the code.
    These are written as a Python list of dictionaries.
    This is useful for featuring specific jobs that aren't in the database.
    """
    static_jobs = [
        {
            'id': 's1', # Unique ID for static jobs
            'title': 'Senior Product Manager',
            'company': 'Slack Technologies, LLC',
            'location': 'New York (Remote)',
            'job_type': 'Full Time',
            'work_setup': 'Remote',
            'level': 'Senior Level',
            'salary_range': '$120,000 - $178,000 / Yearly',
            'company_size': '1-10 employees',
            'industry': 'Software Industry',
            'skills': 'Product Management, Agile, Slack API',
            'description': 'Leading product strategies for team communication tools.',
            'role_description': 'You will take ownership of specific Slack features.',
            'logo_color': '#e01e5a', # Slack brand color
            'time_ago': 'Static Post',
        },
        {
            'id': 's2',
            'title': 'UI Designer',
            'company': 'Telegram FZ LLC',
            'location': 'Dubai (Remote)',
            'job_type': 'Full Time',
            'work_setup': 'Remote',
            'level': 'Senior Level',
            'salary_range': '$90,000 - $140,000 / Yearly',
            'company_size': '10-50 employees',
            'industry': 'Messaging App',
            'skills': 'UI/UX, Figma, Vector Design',
            'description': 'Designing the world\'s fastest messaging interface.',
            'role_description': 'Create beautiful and functional designs for millions of users.',
            'logo_color': '#2AABEE', # Telegram brand color
            'time_ago': 'Static Post',
        }
    ]

    """
    Step 3: Combine both sources into a single 'jobs' list.
    We convert the database QuerySet to a list first, then add our static jobs.
    """
    all_jobs = db_jobs + static_jobs

    """
    Step 4: Handle time logic for database jobs.
    Refresh the 'time_ago' calculation for jobs coming from the DB.
    """
    for job in db_jobs:
        diff = timezone.now() - job.posted_date
        hours = diff.total_seconds() // 3600
        if hours < 1:
            job.time_ago = "just now"
        elif hours < 24:
            job.time_ago = f"{int(hours)} hours ago"
        else:
            job.time_ago = f"{int(hours//24)} days ago"

    # Decide which job to show in the details panel (the first one)
    selected_job = all_jobs[0] if all_jobs else None

    """
    Step 5: Send the combined list to the HTML template.
    We use a dictionary called 'context' to pass data to the front-end.
    """
    context = {
        'jobs': all_jobs,
        'selected_job': selected_job,
    }
    
    return render(request, 'jobs/index.html', context)
