import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase

from task_manager.forms import RegisterForm, TaskForm, TaskNameSearchForm
from task_manager.models import Position, TaskType, Task


class RegisterFormTest(TestCase):
    def setUp(self) -> None:
        self.position = Position.objects.create(name="Developer")
        self.form_data = {
            "username": "test_worker",
            "password1": "worker12345",
            "password2": "worker12345",
            "position": self.position,
            "email": "test@email.com",
            "first_name": "John",
            "last_name": "Doe",
        }

    def test_user_register_form(self):
        form = RegisterForm(data=self.form_data)
        self.assertTrue(form.is_valid())
        for key in form.cleaned_data:
            self.assertEqual(form.cleaned_data[key], self.form_data[key])


class TaskFormTest(TestCase):
    def setUp(self) -> None:
        self.task_type = TaskType.objects.create(name="Refactoring")
        self.position = Position.objects.create(name="Developer")
        self.user = get_user_model().objects.create_user(
            username="test_worker",
            password="worker12345",
            first_name="John",
            last_name="Doe",
            email="test@email.com",
            position=self.position,
        )
        self.form_data = {
            "name": "Implement API",
            "description": "Develop RESTful API",
            "deadline": datetime.date.today(),
            "is_completed": False,
            "priority": "H",
            "task_type": self.task_type,
            "assignees": [self.user],
        }

    def test_task_creating_form(self):
        form = TaskForm(data=self.form_data, user=self.user)
        self.assertTrue(form.is_valid())
        for key in form.cleaned_data:
            first = form.cleaned_data[key]
            second = self.form_data[key]
            if key == "assignees":
                first = list(first)
            self.assertEqual(first, second)

    def test_task_update_form(self):
        task = Task.objects.create(
            name="Test Task",
            description="This is a test task.",
            deadline=datetime.date.today(),
            is_completed=False,
            priority="H",
            task_type=self.task_type,
            assignor=self.user,
        )
        updated_data = {
            "name": "Updated Task",
            "description": "This task has been updated.",
            "deadline": datetime.date.today(),
            "is_completed": True,
            "priority": "L",
            "task_type": self.task_type.id,
            "assignees": [self.user],
        }
        form = TaskForm(data=updated_data, instance=task, user=self.user)
        self.assertTrue(form.is_valid())
        form.save()
        updated_task = Task.objects.get(id=task.id)
        self.assertEqual(updated_task.name, "Updated Task")
        self.assertEqual(
            updated_task.description, "This task has been updated."
        )
        self.assertTrue(updated_task.is_completed)
        self.assertEqual(updated_task.priority, "L")


class TaskNameSearchFormTest(TestCase):
    def test_valid_form(self):
        data = {"name": "TestTask"}
        form = TaskNameSearchForm(data=data)
        self.assertTrue(form.is_valid())

    def test_empty_form(self):
        data = {"name": ""}
        form = TaskNameSearchForm(data=data)
        self.assertTrue(form.is_valid())

    def test_form_without_data(self):
        form = TaskNameSearchForm()
        self.assertFalse(form.is_valid())
