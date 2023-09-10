from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import CheckboxSelectMultiple

from task_manager.models import Task, Worker, Position

User = get_user_model()


class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.required = True

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
        exclude = ("assignor",)

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


class TaskNameSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by task name..."}
        ),
    )
