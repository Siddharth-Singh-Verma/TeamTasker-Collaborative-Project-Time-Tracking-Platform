from django.contrib import admin
from .models import Project, Task, TimeEntry


admin.site.register(Project)
admin.site.register(Task)   
admin.site.register(TimeEntry)
# Register your models here.
