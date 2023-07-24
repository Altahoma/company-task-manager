from django.test import TestCase, Client
from django.urls import reverse

from task_manager.models import Task, TaskType, Worker, Position


class PrivetTestCase(TestCase):
    def test_worker_list_view(self):
        response = self.client.get(reverse("task_manager:worker-list"))
        self.assertNotEqual(response.status_code, 200)

    def test_position_list_view(self):
        response = self.client.get(reverse("task_manager:position-list"))
        self.assertNotEqual(response.status_code, 200)

    def test_task_list_view(self):
        response = self.client.get(reverse("task_manager:task-list"))
        self.assertNotEqual(response.status_code, 200)

    def test_task_create_view(self):
        response = self.client.get(reverse("task_manager:task-create"))
        self.assertNotEqual(response.status_code, 200)

    def test_task_update_view(self):
        response = self.client.get(
            reverse("task_manager:task-update", kwargs={"pk": 1})
        )
        self.assertNotEqual(response.status_code, 200)


class PrivetTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.position = Position.objects.create(name="Developer")
        self.user = Worker.objects.create_user(
            username="test_worker",
            password="worker12345",
            position=self.position,
        )
        self.client.login(username="test_worker", password="worker12345")
        self.task_type = TaskType.objects.create(name="Refactoring")
        self.task = Task.objects.create(
            name="Test Task",
            description="Test Description",
            deadline="2023-01-01",
            is_completed=False,
            priority="M",
            task_type=self.task_type,
            assignor=self.user,
        )

    def test_worker_list_view(self):
        response = self.client.get(reverse("task_manager:worker-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "worker_list.html")

    def test_position_list_view(self):
        response = self.client.get(reverse("task_manager:position-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "position_list.html")

    def test_task_list_view(self):
        response = self.client.get(reverse("task_manager:task-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "task_list.html")

    def test_task_create_view(self):
        response = self.client.get(reverse("task_manager:task-create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "task_form.html")

    def test_task_update_view(self):
        response = self.client.get(
            reverse("task_manager:task-update", kwargs={"pk": self.task.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "task_form.html")
