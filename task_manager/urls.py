from django.urls import path

from task_manager.views import (
    WorkerListView,
    PositionListView,
    TaskTypeListView,
    TaskListView,
    TaskCreateView,
    IndexView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("positions/", PositionListView.as_view(), name="position-list"),
    path("task_types/", TaskTypeListView.as_view(), name="task-type-list"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
]

app_name = "task_manager"
