
from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(User, related_name='projects')

    def __str__(self):
        return self.name


class Task(models.Model):
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


class TimeEntry(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='time_entries')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    hours_spent = models.DecimalField(max_digits=5, decimal_places=2)  # e.g., 3.5 hours

    def __str__(self):
        return f"{self.user.username} - {self.task.title} - {self.hours_spent}h"

# core/models.py
class Activity(models.Model):
    ACTION_CHOICES = [
        ('create_project', 'Created a project'),
        ('add_task', 'Added a task'),
        ('update_task', 'Updated a task'),
        ('delete_task', 'Deleted a task'),
        ('invite_user', 'Invited a user'),
        # You can add more
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    action = models.CharField(max_length=50, choices=ACTION_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} {self.get_action_display()} in {self.project.name}"
