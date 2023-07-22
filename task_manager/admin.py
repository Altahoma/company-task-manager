from django.contrib import admin
from .models import Task, TaskType, Worker, Position


admin.site.register(Task)
admin.site.register(TaskType)
admin.site.register(Worker)
admin.site.register(Position)
