from django.contrib import admin
from .models import Project, Task, TimeEntry, Activity


admin.site.register(Project)
admin.site.register(Task)   
admin.site.register(TimeEntry)
admin.site.register(Activity)

# Register your models here.
