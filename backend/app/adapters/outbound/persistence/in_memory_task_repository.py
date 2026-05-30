from app.application.ports.task_repository import TaskRepository
from app.domain.task import Task


class InMemoryTaskRepository(TaskRepository):
    """Simple adapter that can be replaced by SQL/NoSQL without changing use cases."""

    def __init__(self) -> None:
        self._tasks: dict[str, Task] = {}

    def save(self, task: Task) -> Task:
        self._tasks[task.id] = task
        return task

    def find_all(self) -> list[Task]:
        return list(self._tasks.values())

    def find_by_id(self, task_id: str) -> Task | None:
        return self._tasks.get(task_id)
