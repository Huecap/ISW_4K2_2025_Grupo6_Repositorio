import React from 'react';
import Card from '../components/ui/card';

// Cupos fijos por actividad (fallback si no viene a.cupoMax desde App.jsx)
const CUPOS_FIJOS = { Safari: 8, Tirolesa: 10, Palestra: 12, Jardinería: 12 };

export default function SelectionPage({
  activities,
  selectedActivity,
  handleActivitySelect,
  numParticipants,
  setNumParticipants,
  handleStartEnrollment,
}) {
  return (
    <div className="selection-page">
      <header className="selection-header">
        <h1 className="selection-title">¡Reserva tu Aventura en EcoHarmony Park!</h1>
        <p className="selection-sub">1. Elige una actividad para comenzar la inscripción.</p>
      </header>

      <div className="cards-container">
        {activities.map((a, idx) => {
          const cupoMax = a.cupoMax ?? CUPOS_FIJOS[a.title] ?? CUPOS_FIJOS[a.actividad];
          const totalDisponibles = (a.turnos || []).reduce(
            (acc, t) => acc + (t.cupo_disponible || 0),
            0
          );
          const turnosConCupo = (a.turnos || []).filter(
            (t) => (t.cupo_disponible || 0) > 0
          ).length;
          const tieneTurnoSuficiente = (a.turnos || []).some(
            (t) => (t.cupo_disponible || 0) >= numParticipants
          );

          const isSelected = selectedActivity && selectedActivity.title === a.title;

          return (
            <div
              key={idx}
              className={`card-wrapper ${!tieneTurnoSuficiente ? 'card--disabled' : ''}`}
              title={
                !tieneTurnoSuficiente
                  ? `No hay turnos con ${numParticipants} lugar(es) disponibles`
                  : ''
              }
              onClick={() => {
                if (tieneTurnoSuficiente) handleActivitySelect(a);
              }}
              style={{
                cursor: tieneTurnoSuficiente ? 'pointer' : 'not-allowed',
                opacity: tieneTurnoSuficiente ? 1 : 0.5,
              }}
            >
              <div
                className="card-content"
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'space-between',
                  gap: '16px',
                }}
              >
                <Card
                  icon={a.icon}
                  title={a.title}
                  description={`${a.description} · ${turnosConCupo} horarios con cupo · ${totalDisponibles} lugares totales`}
                  isSelected={isSelected}
                />

                <div
                  className="card-badges"
                  style={{
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'flex-end',
                    gap: '4px',
                    minWidth: '120px',
                  }}
                >
                  {cupoMax != null && (
                    <span
                      className="cupo-max-tag"
                      style={{
                        fontSize: '0.9rem',
                        color: '#475569', // slate-600 aprox
                        fontWeight: 600,
                        whiteSpace: 'nowrap',
                      }}
                    >
                      Cupo máx: {cupoMax}
                    </span>
                  )}

                  
                </div>
              </div>
            </div>
          );
        })}
      </div>

      {selectedActivity && (
        <div className="selection-controls">
          <label className="participants-label">
            <span>Cantidad de Participantes:</span>
            <input
              type="number"
              value={numParticipants}
              onChange={(e) =>
                setNumParticipants(Math.max(1, parseInt(e.target.value) || 1))
              }
              min="1"
              className="participants-input"
            />
          </label>

          <button onClick={handleStartEnrollment} className="btn btn--primary">
            2. Continuar a la Inscripción ({numParticipants} P.)
          </button>
        </div>
      )}
    </div>
  );
}
