from flask import Flask
from flask_cors import CORS

from app.adapters.inbound.http.task_controller import create_task_blueprint
from app.adapters.outbound.persistence.in_memory_task_repository import InMemoryTaskRepository
from app.application.use_cases.task_service import TaskService


def create_app() -> Flask:
    app = Flask(__name__)
    CORS(app)

    repository = InMemoryTaskRepository()
    service = TaskService(repository)
    app.register_blueprint(create_task_blueprint(service))

    @app.get("/api/health")
    def health_check():
        return {"status": "ok", "architecture": "hexagonal"}

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
