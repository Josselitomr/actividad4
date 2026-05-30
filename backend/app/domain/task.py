from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from uuid import uuid4


class TaskStatus(str, Enum):
    """Valid lifecycle states for a task."""

    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"


@dataclass(slots=True)
class Task:
    """Domain entity that keeps business rules independent from frameworks."""

    title: str
    description: str
    priority: int
    status: TaskStatus = TaskStatus.PENDING
    id: str = field(default_factory=lambda: str(uuid4()))
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def __post_init__(self) -> None:
        title = self.title.strip()
        description = self.description.strip()
        if not title:
            raise ValueError("Task title is required")
        if not 1 <= self.priority <= 5:
            raise ValueError("Task priority must be between 1 and 5")
        self.title = title
        self.description = description

    def move_to(self, status: TaskStatus) -> None:
        """Change status while keeping transition validation in the domain."""

        if self.status == TaskStatus.DONE and status != TaskStatus.DONE:
            raise ValueError("Completed tasks cannot be reopened")
        self.status = status

    def to_dict(self) -> dict[str, str | int]:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "status": self.status.value,
            "createdAt": self.created_at.isoformat(),
        }
