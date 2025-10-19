import React from 'react';
import Card from '../components/ui/card';

const SelectionPage = ({ activities, selectedActivity, handleActivitySelect, numParticipants, setNumParticipants, handleStartEnrollment }) => (
  <div className="selection-page">
    <header className="selection-header">
      <h1 className="selection-title">¡Reserva tu Aventura en EcoHarmony Park!</h1>
      <p className="selection-sub">1. Elige una actividad para comenzar la inscripción.</p>
    </header>

    <div className="cards-container">
      {activities.map((activity, index) => (
        <Card
          key={index}
          icon={activity.icon}
          title={activity.title}
          description={activity.description}
          isSelected={selectedActivity && selectedActivity.title === activity.title}
          onClick={() => handleActivitySelect(activity)}
        />
      ))}
    </div>

    {selectedActivity && (
      <div className="selection-controls">
        <label className="participants-label">
          <span>Cantidad de Participantes:</span>
          <input
            type="number"
            value={numParticipants}
            onChange={(e) => setNumParticipants(Math.max(1, parseInt(e.target.value) || 1))}
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

export default SelectionPage;
