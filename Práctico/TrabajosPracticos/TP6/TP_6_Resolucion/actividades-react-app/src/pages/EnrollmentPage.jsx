import React, { useEffect, useMemo, useState } from 'react';
import ParticipantCard from '../components/ui/ParticipantCard';
import TermsModal from '../components/ui/TermsModal';
import { postInscribir } from '../api';

// Constantes de validación
const DNI_REGEX = /^\d{7,8}$/;
const TALLE_OPCIONES = ['XS', 'S', 'M', 'L', 'XL', 'XXL'];

export default function EnrollmentPage({
  selectedActivity,
  numParticipants,
  requiresSizeSet,
  onBack,
  onSuccess, // ← callback para volver y refrescar
}) {
  const requiresSize = useMemo(
    () => requiresSizeSet.has(selectedActivity.title),
    [requiresSizeSet, selectedActivity]
  );
  const edadMinima = selectedActivity.edad_minima ?? 0;

  const initialParticipantsState = Array.from({ length: numParticipants }, () => ({
    nombre: '',
    dni: '',
    edad: '',
    talla: '',
    acepta_tyc: false,
  }));

  const [participants, setParticipants] = useState(initialParticipantsState);
  const [selectedSchedule, setSelectedSchedule] = useState('');
  const [acceptTerms, setAcceptTerms] = useState(false);
  const [showModal, setShowModal] = useState(false);

  const turnosConCupo = selectedActivity.turnos ?? [];

  const handleParticipantChange = (index, name, value) => {
    setParticipants((prev) => {
      const copy = [...prev];
      copy[index] = { ...copy[index], [name]: value };
      return copy;
    });
  };

  // Si cambia la cantidad de participantes y el turno elegido queda corto, lo limpiamos
  useEffect(() => {
    const elegido = (selectedActivity.turnos || []).find((t) => t.hora === selectedSchedule);
    if (elegido && Number(elegido.cupo_disponible ?? 0) < numParticipants) {
      setSelectedSchedule('');
    }
  }, [numParticipants, selectedActivity, selectedSchedule]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const errors = [];

    // 1) Horario + TyC
    if (!selectedSchedule) errors.push('Debe seleccionar un horario.');
    if (!acceptTerms) errors.push('Debe aceptar los términos y condiciones.');

    // 2) Validaciones por participante (recomputadas en cada submit)
    const requiresSizeFlag = selectedActivity.requiere_vestimenta === true;
    const edadMin = selectedActivity.edad_minima ?? 0;

    participants.forEach((p, i) => {
      const idx = i + 1;

      // DNI
      const dni = String(p.dni || '').trim();
      if (!DNI_REGEX.test(dni)) {
        errors.push(`(#${idx}) DNI inválido: use 7 u 8 dígitos numéricos.`);
      }

      // Edad
      const edad = Number(p.edad);
      if (Number.isNaN(edad)) {
        errors.push(`(#${idx}) Edad inválida.`);
      } else {
        if (edad < Math.max(1, edadMin)) errors.push(`(#${idx}) Edad mínima ${Math.max(1, edadMin)}.`);
        if (edad > 100) errors.push(`(#${idx}) Edad máxima 100.`);
      }

      // Talle (solo si corresponde)
      if (requiresSizeFlag) {
        const talla = String(p.talla || '').toUpperCase();
        if (!TALLE_OPCIONES.includes(talla)) {
          errors.push(`(#${idx}) Seleccione un talle válido (XS–XXL).`);
        }
      }
    });

    // 3) Guard de cupos por horario
    const turnoElegido = (selectedActivity.turnos || []).find((t) => t.hora === selectedSchedule);
    if (!turnoElegido) {
      errors.push('Seleccione un horario válido.');
    } else if (Number(turnoElegido.cupo_disponible ?? 0) < numParticipants) {
      errors.push(`El horario ${turnoElegido.hora} no tiene cupos para ${numParticipants} persona(s).`);
    }

    if (errors.length) {
      alert('Errores de Validación:\n' + errors.join('\n'));
      return;
    }

    // 4) Payload EXACTO
    const payload = {
      actividad: selectedActivity.title,
      horario: selectedSchedule, // "HH:MM"
      visitantes: participants.map((p) => ({
        nombre: p.nombre,
        dni: String(p.dni || '').trim(),
        edad: Number(p.edad || 0),
        talla_vestimenta: requiresSizeFlag ? String(p.talla || '').toUpperCase() : null,
        acepta_tyc: true,
      })),
    };

    try {
      const res = await fetch('http://localhost:5000/inscribir', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      });
      const data = await res.json().catch(() => ({}));

      let huboExito = false;

      if (res.status === 201) {
        huboExito = true;
        alert('✅ Todas las inscripciones fueron exitosas.');
      } else if (res.status === 207) {
        const okList = (data.resultados || []).filter((r) => r.ok).map((r) => r.dni);
        const failList = (data.resultados || [])
          .filter((r) => !r.ok)
          .map((r) => `DNI ${r.dni}: ${r.mensaje || r.error}`);
        huboExito = okList.length > 0;
        alert(
          `⚠️ Resultado parcial:\n✔️ OK: ${okList.join(', ') || '—'}\n❌ Fallas:\n${
            failList.join('\n') || '—'
          }`
        );
      } else if (!res.ok) {
        const detalle = Array.isArray(data?.resultados)
          ? data.resultados.map((r) => `DNI ${r.dni}: ${r.mensaje || r.error}`).join('\n')
          : data?.mensaje || `Error del servidor: ${res.status}`;
        alert(`❌ Error (${res.status}):\n${detalle}`);
      } else {
        huboExito = true;
      }

      if (huboExito && typeof onSuccess === 'function') {
        await onSuccess(); // ← vuelve a selección y refresca disponibilidad
      }
    } catch (err) {
      console.error(err);
      alert('❌ No se pudo conectar con la API.');
    }
  };

  // T&C: checkbox + modal
  const handleTermsCheckboxChange = () => {
    if (acceptTerms) setAcceptTerms(false);
    else setShowModal(true);
  };

  const activityTitle = selectedActivity.title;
  const requiresSizeNotice = requiresSize
    ? 'Nota: Esta actividad requiere ingresar la Talla de Vestimenta.'
    : 'Nota: Esta actividad NO requiere talle de vestimenta.';

  return (
    <div className="enrollment-page">
      <button onClick={onBack} className="btn btn--muted btn--back">
        ← Volver a Selección
      </button>

      <h2 className="enrollment-title">
        Inscripción a: {activityTitle} ({numParticipants} Persona/s) · Edad mínima: {edadMinima || 0}
      </h2>

      <form onSubmit={handleSubmit} className="enrollment-form">
        <section className="panel panel--info">
          <h3>1. Horario y Cupos</h3>
          <div className="panel-row">
            <label className="form-field">
              <span className="form-field__label">Seleccionar Horario Disponible:</span>
              <select
                value={selectedSchedule}
                onChange={(e) => setSelectedSchedule(e.target.value)}
                required
                className="form-field__input"
              >
                <option value="">-- Elige un Horario --</option>
                {(selectedActivity.turnos || []).map((t) => {
                  const disponibles = Number(t.cupo_disponible ?? 0);
                  const insuficiente = disponibles < numParticipants;
                  return (
                    <option
                      key={t.hora}
                      value={t.hora}
                      disabled={insuficiente}
                      title={
                        insuficiente
                          ? `Solo ${disponibles} lugar(es). Necesitás ${numParticipants}.`
                          : ''
                      }
                    >
                      {t.hora} · {disponibles}/{t.cupo_max} cupos
                      {insuficiente ? ` (insuficiente para ${numParticipants})` : ''}
                    </option>
                  );
                })}
              </select>
            </label>
            <p className="note">{requiresSizeNotice}</p>
          </div>
        </section>

        <section className="panel">
          <h3 className="section-title">2. Datos de los Participantes</h3>
          {Array.from({ length: numParticipants }).map((_, index) => (
            <ParticipantCard
              key={index}
              index={index}
              data={participants[index]}
              onChange={handleParticipantChange}
              activity={activityTitle}
              requiresSize={requiresSize}
              edadMinima={edadMinima}
            />
          ))}
        </section>

        <section className="panel panel--danger">
          <label className="terms-row" style={{ alignItems: 'center' }}>
            <input type="checkbox" checked={acceptTerms} onChange={handleTermsCheckboxChange} required />
            <span style={{ marginLeft: 8 }}>
              Acepto los{' '}
              <button
                type="button"
                className="link"
                onClick={() => setShowModal(true)}
                style={{
                  textDecoration: 'underline',
                  color: '#2563eb',
                  background: 'transparent',
                  border: 'none',
                  padding: 0,
                  cursor: 'pointer',
                }}
              >
                términos y condiciones
              </button>{' '}
              específicos para la actividad “{activityTitle}”.
            </span>
          </label>
        </section>

        <div className="form-actions">
          <button type="submit" className="btn btn--primary btn--large">
            Confirmar Inscripción
          </button>
        </div>
      </form>

      {showModal && (
        <TermsModal
          actividad={activityTitle}
          onAccept={() => {
            setAcceptTerms(true);
            setShowModal(false);
          }}
          onClose={() => setShowModal(false)}
        />
      )}
    </div>
  );
}
