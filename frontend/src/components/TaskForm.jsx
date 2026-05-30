import { useState } from 'react';

const initialForm = { title: '', description: '', priority: 3 };

export function TaskForm({ onSubmit }) {
  const [form, setForm] = useState(initialForm);

  const updateField = (event) => {
    const { name, value } = event.target;
    setForm((current) => ({ ...current, [name]: name === 'priority' ? Number(value) : value }));
  };

  const submit = async (event) => {
    event.preventDefault();
    await onSubmit(form);
    setForm(initialForm);
  };

  return (
    <form className="task-form" onSubmit={submit}>
      <label>
        Título
        <input name="title" value={form.title} onChange={updateField} placeholder="Ej. Diseñar puertos" required />
      </label>
      <label>
        Descripción
        <textarea name="description" value={form.description} onChange={updateField} placeholder="Detalle de la actividad" />
      </label>
      <label>
        Prioridad
        <input name="priority" type="number" min="1" max="5" value={form.priority} onChange={updateField} />
      </label>
      <button type="submit">Crear tarea</button>
    </form>
  );
}
