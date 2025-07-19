# core/utils.py
from .models import Activity

def log_activity(user, project, action):
    Activity.objects.create(user=user, project=project, action=action)
