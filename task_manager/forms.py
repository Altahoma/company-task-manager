from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import CheckboxSelectMultiple

from task_manager.models import Task, Worker

User = get_user_model()


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "email",
            "position",
        ]


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        exclude = ("is_completed", "assignor")

        widgets = {
            "deadline": forms.DateInput(attrs={"type": "date"}),
            "description": forms.Textarea(attrs={"rows": 2}),
            "assignees": CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields["assignees"].queryset = Worker.objects.filter(
            position=user.position
        )
        # self.fields['assignees'].queryset = Worker.objects.filter(
        #     position__name='Developer')
