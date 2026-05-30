# Actividad 4 · Aplicación Web con Arquitectura Hexagonal

Aplicación full stack para gestionar entregables académicos. El problema elegido es la planificación de tareas de una entrega: crear actividades, priorizarlas, moverlas por estado y evitar reglas inválidas como reabrir una tarea finalizada.

## Tecnologías

- **Backend:** Flask + Python.
- **Frontend:** React + Vite.
- **Persistencia:** adaptador en memoria, reemplazable por SQL/NoSQL sin modificar casos de uso.

## Arquitectura Hexagonal

```text
backend/app
├── domain/                         # Entidades y reglas de negocio puras
├── application/
│   ├── ports/                       # Contratos que aíslan infraestructura
│   └── use_cases/                   # Casos de uso de la aplicación
└── adapters/
    ├── inbound/http/                # API REST Flask
    └── outbound/persistence/        # Implementación de repositorio
```

La regla de dependencia apunta hacia el dominio: los controladores HTTP conocen los casos de uso, los casos de uso conocen puertos abstractos y el repositorio concreto implementa esos puertos.

## Evidencia de Código Limpio, Refactorización y SOLID

- **Responsabilidad única:** `Task`, `TaskService`, `TaskRepository` y `InMemoryTaskRepository` tienen responsabilidades separadas.
- **Abierto/Cerrado:** se puede agregar un repositorio SQL implementando `TaskRepository` sin cambiar `TaskService`.
- **Inversión de dependencias:** `TaskService` recibe el puerto `TaskRepository`, no una clase de infraestructura.
- **Código limpio:** nombres expresivos, validaciones de dominio centralizadas y componentes React pequeños.
- **Refactorización:** la lógica de creación/listado/cambio de estado se extrajo de la capa HTTP hacia casos de uso reutilizables.

## Ejecutar Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
flask --app app.main run --debug
```

Endpoints principales:

- `GET /api/health`
- `GET /api/tasks`
- `POST /api/tasks`
- `PATCH /api/tasks/{id}/status`

## Ejecutar Frontend

```bash
cd frontend
npm install
npm run dev
```

La URL del backend se puede configurar con `VITE_API_URL`. Por defecto usa `http://localhost:5000/api`.

## Pruebas

```bash
cd backend
python -m unittest discover -s tests
```
