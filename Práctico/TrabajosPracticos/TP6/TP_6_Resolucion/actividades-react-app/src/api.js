const BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000';

export async function getDisponibilidad() {
  const res = await fetch(`${BASE_URL}/disponibilidad`);
  if (!res.ok) throw new Error('No se pudo obtener la disponibilidad');
  return res.json(); // { items: [ {actividad, requiere_vestimenta, edad_minima, turnos:[{hora,cupo_max,cupo_disponible}]} ] }
}

export async function postInscribir(payload) {
  const res = await fetch(`${BASE_URL}/inscribir`, {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(payload),
  });
  const data = await res.json().catch(() => ({}));
  return { ok: res.ok, status: res.status, data };
}
