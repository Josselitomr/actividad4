const API_URL = import.meta.env.VITE_API_URL ?? 'http://localhost:5000/api';

export async function getTasks() {
  const response = await fetch(`${API_URL}/tasks`);
  if (!response.ok) throw new Error('No se pudieron cargar las tareas');
  return response.json();
}

export async function createTask(task) {
  const response = await fetch(`${API_URL}/tasks`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(task),
  });
  if (!response.ok) throw new Error((await response.json()).message);
  return response.json();
}

export async function updateTaskStatus(taskId, status) {
  const response = await fetch(`${API_URL}/tasks/${taskId}/status`, {
    method: 'PATCH',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ status }),
  });
  if (!response.ok) throw new Error((await response.json()).message);
  return response.json();
}
