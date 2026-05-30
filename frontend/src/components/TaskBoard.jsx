const statusLabels = {
  PENDING: 'Pendiente',
  IN_PROGRESS: 'En progreso',
  DONE: 'Terminada',
};

export function TaskBoard({ tasks, onStatusChange }) {
  if (tasks.length === 0) {
    return <p className="empty-state">Aún no hay tareas. Crea la primera para planear tu entrega.</p>;
  }

  return (
    <section className="task-grid" aria-label="Tablero de tareas">
      {tasks.map((task) => (
        <article className="task-card" key={task.id}>
          <div>
            <span className="badge">Prioridad {task.priority}</span>
            <h3>{task.title}</h3>
            <p>{task.description || 'Sin descripción'}</p>
          </div>
          <label>
            Estado
            <select value={task.status} onChange={(event) => onStatusChange(task.id, event.target.value)}>
              {Object.entries(statusLabels).map(([value, label]) => (
                <option key={value} value={value}>{label}</option>
              ))}
            </select>
          </label>
        </article>
      ))}
    </section>
  );
}
