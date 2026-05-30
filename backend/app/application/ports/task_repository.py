from abc import ABC, abstractmethod

from app.domain.task import Task


class TaskRepository(ABC):
    """Outbound port. Use cases depend on this abstraction, not storage details."""

    @abstractmethod
    def save(self, task: Task) -> Task:
        raise NotImplementedError

    @abstractmethod
    def find_all(self) -> list[Task]:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, task_id: str) -> Task | None:
        raise NotImplementedError
