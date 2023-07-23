from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView

from task_manager.forms import TaskForm, RegisterForm
from task_manager.models import Worker, Position, TaskType, Task


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    template_name = "worker_list.html"


class PositionListView(LoginRequiredMixin, generic.ListView):
    model = Position
    template_name = "position_list.html"


class TaskTypeListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    template_name = "task_type_list.html"


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = "task_list.html"

    def get_queryset(self):
        return Task.objects.filter(assignor=self.request.user)


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "task_form.html"
    success_url = reverse_lazy("task_manager:index")

    # def get_initial(self, *args, **kwargs):
    #     initial = super(TaskCreateView, self).get_initial()
    #     initial['assignor'] = self.request.user
    #     return initial

    def form_valid(self, form):
        form.instance.assignor = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(TaskCreateView, self).get_form_kwargs()
        kwargs.update({"user": self.request.user})
        return kwargs


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("task_manager:index")
        return super().dispatch(*args, **kwargs)
