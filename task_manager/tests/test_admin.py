import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase, Client

from task_manager.models import Task, Position, Worker, TaskType


class AdminSiteTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin", password="admin12345"
        )
        self.client.force_login(self.admin_user)

        self.position = Position.objects.create(name="Manager")
        self.worker = Worker.objects.create_user(
            username="worker",
            password="worker12345",
            first_name="John",
            last_name="Doe",
            position=self.position,
        )
        self.task_type = TaskType.objects.create(name="Task Type 1")
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

    def test_task_admin(self):
        response = self.client.get("/admin/task_manager/task/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test task")
        self.assertContains(response, "Task Type 1")
        self.assertContains(response, "H")
        self.assertContains(response, "worker")

    def test_user_admin(self):
        response = self.client.get('/admin/task_manager/worker/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'worker')
        self.assertContains(response, 'John')
        self.assertContains(response, 'Doe')
        self.assertContains(response, 'User')
        self.assertContains(response, 'Manager')
