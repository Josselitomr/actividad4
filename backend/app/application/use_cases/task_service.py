from app.application.ports.task_repository import TaskRepository
from app.domain.task import Task, TaskStatus


class TaskService:
    """Application service that orchestrates task use cases."""

    def __init__(self, repository: TaskRepository) -> None:
        self._repository = repository

    def create_task(self, title: str, description: str, priority: int) -> Task:
        task = Task(title=title, description=description, priority=priority)
        return self._repository.save(task)

    def list_tasks(self) -> list[Task]:
        return sorted(
            self._repository.find_all(),
            key=lambda task: (task.status == TaskStatus.DONE, -task.priority, task.created_at),
        )

    def update_status(self, task_id: str, status: str) -> Task:
        task = self._repository.find_by_id(task_id)
        if task is None:
            raise LookupError("Task was not found")
        task.move_to(TaskStatus(status))
        return self._repository.save(task)
