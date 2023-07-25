from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import Task, TaskType, Worker, Position

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "position")


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'task_type', 'priority', 'deadline', 'assignor')


admin.site.register(TaskType)
admin.site.register(Position)
