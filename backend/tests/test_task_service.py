import unittest

from app.adapters.outbound.persistence.in_memory_task_repository import InMemoryTaskRepository
from app.application.use_cases.task_service import TaskService
from app.domain.task import TaskStatus


class TaskServiceTest(unittest.TestCase):
    def setUp(self) -> None:
        self.service = TaskService(InMemoryTaskRepository())

    def test_create_task_trims_title_and_sets_pending_status(self) -> None:
        task = self.service.create_task("  Preparar demo ", "Arquitectura hexagonal", 5)

        self.assertEqual("Preparar demo", task.title)
        self.assertEqual(TaskStatus.PENDING, task.status)

    def test_done_task_cannot_be_reopened(self) -> None:
        task = self.service.create_task("Entregar", "Subir al repositorio", 4)
        self.service.update_status(task.id, "DONE")

        with self.assertRaises(ValueError):
            self.service.update_status(task.id, "IN_PROGRESS")


if __name__ == "__main__":
    unittest.main()
