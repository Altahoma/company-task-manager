import datetime

from django.test import TestCase
from django.contrib.auth import get_user_model

from task_manager.models import Position, TaskType, Task


class PositionTest(TestCase):
    def setUp(self) -> None:
        self.position = Position.objects.create(name="Developer")

    def test_position_str_method(self):
        self.assertEqual(str(self.position), "Developer")


class WorkerTest(TestCase):
    def setUp(self) -> None:
        self.position = Position.objects.create(name="Developer")
        self.worker = get_user_model().objects.create_user(
            username="test_worker",
            password="worker12345",
            first_name="John",
            last_name="Doe",
            email="test@email.com",
            position=self.position,
        )

    def test_worker_str_method(self):
        self.assertEqual(str(self.worker), "test_worker (Developer)")


class TaskTypeTest(TestCase):
    def setUp(self) -> None:
        self.task_type = TaskType.objects.create(name="Refactoring")

    def test_task_type_str_method(self):
        self.assertEqual(str(self.task_type), "Refactoring")


class TaskTest(TestCase):
    def setUp(self) -> None:
        self.task_type = TaskType.objects.create(name="Refactoring")
        self.position = Position.objects.create(name="Developer")
        self.worker = get_user_model().objects.create_user(
            username="test_worker",
            password="worker12345",
            first_name="John",
            last_name="Doe",
            email="test@email.com",
            position=self.position,
        )
        self.task = Task.objects.create(
            name="Test task",
            description="Test description",
            deadline=datetime.date.today(),
            is_completed=False,
            priority="H",
            task_type=self.task_type,
            assignor=self.worker,
        )
        self.task.assignees.add(self.worker)

    def test_task_str_method(self):
        self.assertEqual(str(self.task), "Test task")
