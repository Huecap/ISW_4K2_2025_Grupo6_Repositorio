import React, { useState } from 'react';
import ParticipantCard from '../components/ui/ParticipantCard';
import TermsModal from '../components/ui/TermsModal'; // Asegurate de tener este componente

const REQUIRES_SIZE = ['Tirolesa', 'Palestra'];

const EnrollmentPage = ({ selectedActivity, numParticipants, onBack }) => {
  const initialParticipantsState = Array(numParticipants)
    .fill()
    .map(() => ({ nombre: '', dni: '', edad: '', tnalla: '' , acepta_tyc: ''}));

  const [participants, setParticipants] = useState(initialParticipantsState);
  const [selectedSchedule, setSelectedSchedule] = useState('');
  const [acceptTerms, setAcceptTerms] = useState(false);
  const [showModal, setShowModal] = useState(false);

  const handleParticipantChange = (index, name, value) => {
    const newParticipants = [...participants];
    newParticipants[index] = { ...newParticipants[index], [name]: value };
    setParticipants(newParticipants);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const errors = [];

    if (!selectedSchedule) {
      errors.push('Debe seleccionar un horario.');
    } else if (selectedSchedule === '14:00') {
      errors.push(
        'El horario seleccionado (14:00 PM) no tiene cupos disponibles o la actividad no está disponible.'
      );
    }

    if (!acceptTerms) {
      errors.push('Debe aceptar los términos y condiciones.');
    }

    const requiresSize = REQUIRES_SIZE.includes(selectedActivity.title);
    if (requiresSize && participants.some((p) => !p.talla)) {
      errors.push(
        'La actividad requiere talle de vestimenta para todos los participantes.'
      );
    }

    if (errors.length > 0) {
      alert('Errores de Validación:\n' + errors.join('\n'));
      return;
    }

    // ✅ Datos correctos que espera tu API Flask
    const payload = {
      actividad: selectedActivity.title,
      horario: selectedSchedule,
      visitantes: participants.map((p) => ({
        nombre: p.nombre,
        dni: p.dni,
        edad: p.edad,
        talla_vestimenta: p.talla,
        acepta_tyc: true, // siempre TRUE
      })),
    };

   try {
    const response = await fetch('http://localhost:5000/inscribir', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
    });

    // 1. Siempre intenta leer la respuesta JSON, sea de éxito o de error.
    const data = await response.json();

    // 2. AHORA sí, verifica si la respuesta fue exitosa (status 200-299).
    if (!response.ok) {
        // 3. Si no fue exitosa, lanza un error USANDO el mensaje del backend.
        throw new Error(data.mensaje || `Error del servidor: ${response.status}`);
    }

    // Si el código llega aquí, la inscripción fue exitosa.
    console.log('Respuesta del servidor:', data);
    alert(`✅ ${data.mensaje || 'Inscripción enviada con éxito.'}`);

    // Limpieza del formulario
    setParticipants(initialParticipantsState);
    setSelectedSchedule('');
    setAcceptTerms(false);

} catch (error) {
    console.error('Error al procesar la inscripción:', error);
    // 4. Ahora el 'error.message' contiene el texto útil del backend.
    alert(`❌ Error: ${error.message}`);
}}

  const activityTitle = selectedActivity.title;
  const requiresSizeNotice = REQUIRES_SIZE.includes(activityTitle)
    ? 'Nota: Esta actividad requiere ingresar la Talla de Vestimenta.'
    : 'Nota: Esta actividad NO requiere talle de vestimenta.';

  // Manejo del checkbox + modal de términos
  const handleTermsCheckboxChange = () => {
    if (acceptTerms) {
      setAcceptTerms(false);
    } else {
      setShowModal(true);
    }
  };

  return (
    <div className="enrollment-page">
      <button onClick={onBack} className="btn btn--muted btn--back">
        ← Volver a Selección
      </button>

      <h2 className="enrollment-title">
        Inscripción a: {activityTitle} ({numParticipants} Persona/s)
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
                <option value="9:00">9:00 AM (4 cupos disponibles)</option>
                <option value="11:00">11:00 AM (2 cupos disponibles)</option>
                <option value="14:00" disabled>
                  14:00 PM (Sin cupo disponible)
                </option>
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
            />
          ))}
        </section>

        {/* Términos y condiciones con modal */}
        <section className="panel panel--danger">
          <label className="terms-row" style={{ alignItems: 'center' }}>
            <input
              type="checkbox"
              checked={acceptTerms}
              onChange={handleTermsCheckboxChange}
              required
            />
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
              específicos para la actividad "{activityTitle}".
            </span>
          </label>
        </section>

        <div className="form-actions">
          <button type="submit" className="btn btn--primary btn--large">
            Confirmar Inscripción
          </button>
        </div>
      </form>

      {/* Modal */}
      {showModal && (
        <TermsModal
          onAccept={() => {
            setAcceptTerms(true);
            setShowModal(false);
          }}
          onClose={() => setShowModal(false)}
        />
      )}
    </div>
  );
};

export default EnrollmentPage;
