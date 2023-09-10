from datetime import datetime

from django.db.models import Q

from task_manager.models import Task


def sidebar_data(request):
    if request.user.is_authenticated:
        queryset = Task.objects.filter(
            Q(assignor=request.user) | Q(assignees=request.user)
        ).distinct()

        all_tasks = queryset.count()
        active_tasks = queryset.filter(is_completed=False).count()
        waiting_tasks = (
            queryset.filter(is_completed=False)
            .filter(deadline__lt=datetime.today())
            .count()
        )
        completed_tasks = queryset.filter(is_completed=True).count()

        return {
            "all_tasks": all_tasks,
            "active_tasks": active_tasks,
            "waiting_tasks": waiting_tasks,
            "completed_tasks": completed_tasks,
        }
    return {}
