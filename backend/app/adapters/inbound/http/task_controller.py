from flask import Blueprint, jsonify, request

from app.application.use_cases.task_service import TaskService
from app.domain.task import TaskStatus


def create_task_blueprint(service: TaskService) -> Blueprint:
    blueprint = Blueprint("tasks", __name__, url_prefix="/api/tasks")

    @blueprint.get("")
    def list_tasks():
        return jsonify([task.to_dict() for task in service.list_tasks()])

    @blueprint.post("")
    def create_task():
        payload = request.get_json(silent=True) or {}
        try:
            task = service.create_task(
                title=str(payload.get("title", "")),
                description=str(payload.get("description", "")),
                priority=int(payload.get("priority", 3)),
            )
        except (TypeError, ValueError) as error:
            return jsonify({"message": str(error)}), 400
        return jsonify(task.to_dict()), 201

    @blueprint.patch("/<task_id>/status")
    def update_status(task_id: str):
        payload = request.get_json(silent=True) or {}
        try:
            task = service.update_status(task_id, str(payload.get("status", "")))
        except ValueError:
            allowed = [status.value for status in TaskStatus]
            return jsonify({"message": f"Status must be one of {allowed}"}), 400
        except LookupError as error:
            return jsonify({"message": str(error)}), 404
        return jsonify(task.to_dict())

    return blueprint
