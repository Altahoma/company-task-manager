from task_manager.models import Task
from datetime import datetime


def sidebar_data(request):
    if request.user.is_authenticated:
        queryset = Task.objects.all()

        all_tasks = queryset.count()
        pending_tasks = queryset.filter(assignor=request.user).count()
        active_tasks = queryset.filter(assignees=request.user).count()
        waiting_tasks = (
            queryset.filter(is_completed=False)
            .filter(deadline__lt=datetime.today())
            .count()
        )
        completed_tasks = queryset.filter(is_completed=True).count()

        return {
            "all_tasks": all_tasks,
            "pending_tasks": pending_tasks,
            "active_tasks": active_tasks,
            "waiting_tasks": waiting_tasks,
            "completed_tasks": completed_tasks,
        }
    return {}
