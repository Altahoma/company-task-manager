from django.contrib import admin
from django.urls import path, include

from task_manager.views import RegisterView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path("", include("task_manager.urls", namespace="task_manager")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/register/", RegisterView.as_view(), name="register"),
]
