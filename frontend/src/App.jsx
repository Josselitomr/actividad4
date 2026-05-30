import { useEffect, useMemo, useState } from 'react';
import { TaskBoard } from './components/TaskBoard';
import { TaskForm } from './components/TaskForm';
import { createTask, getTasks, updateTaskStatus } from './services/taskApi';
import './styles.css';

export default function App() {
  const [tasks, setTasks] = useState([]);
  const [error, setError] = useState('');
  const completedCount = useMemo(() => tasks.filter((task) => task.status === 'DONE').length, [tasks]);

  const loadTasks = async () => {
    setTasks(await getTasks());
  };

  useEffect(() => {
    loadTasks().catch((exception) => setError(exception.message));
  }, []);

  const handleCreateTask = async (task) => {
    setError('');
    await createTask(task);
    await loadTasks();
  };

  const handleStatusChange = async (taskId, status) => {
    setError('');
    try {
      await updateTaskStatus(taskId, status);
      await loadTasks();
    } catch (exception) {
      setError(exception.message);
    }
  };

  return (
    <main className="app-shell">
      <section className="hero">
        <div>
          <p className="eyebrow">Arquitectura Hexagonal · React + Flask</p>
          <h1>Gestor académico de entregables</h1>
          <p>
            Organiza tareas, valida reglas de negocio en el dominio y desacopla el frontend del backend
            mediante una API REST limpia.
          </p>
        </div>
        <div className="metric-card">
          <strong>{completedCount}/{tasks.length}</strong>
          <span>tareas terminadas</span>
        </div>
      </section>

      <TaskForm onSubmit={handleCreateTask} />
      {error && <p className="error" role="alert">{error}</p>}
      <TaskBoard tasks={tasks} onStatusChange={handleStatusChange} />
    </main>
  );
}
