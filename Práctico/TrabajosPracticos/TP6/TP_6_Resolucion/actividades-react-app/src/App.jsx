import React, { useState } from 'react';
import SelectionPage from './pages/SelectionPage';
import EnrollmentPage from './pages/EnrollmentPage';
import './styles.css';

const App = () => {
  const [currentPage, setCurrentPage] = useState('selection'); // 'selection' o 'enrollment'
  const [selectedActivity, setSelectedActivity] = useState(null);
  const [numParticipants, setNumParticipants] = useState(1);

  const activities = [
    { icon: '🧗', title: 'Palestra', description: 'Desafía la gravedad y pon a prueba tu fuerza y agilidad en nuestros muros de escalada.' },
    { icon: '🦓', title: 'Safari', description: 'Recorre la reserva natural y captura la vida salvaje en su hábitat. ¡Apto para toda la familia!' },
    { icon: '🦅', title: 'Tirolesa', description: 'Siente la adrenalina al deslizarte a gran velocidad sobre el paisaje. (Requiere talle de vestimenta)' },
    { icon: '🌱', title: 'Jardinería', description: 'Una actividad relajante para conectar con la naturaleza y aprender sobre el cuidado de plantas.' },
  ];

  const handleActivitySelect = (activity) => {
    setSelectedActivity(activity);
  };

  const handleStartEnrollment = () => {
    if (!selectedActivity) {
      alert("Por favor, selecciona una actividad antes de continuar.");
      return;
    }
    if (numParticipants < 1) {
      alert("La cantidad de participantes debe ser al menos 1.");
      return;
    }
    setCurrentPage('enrollment');
  };

  return (
    <div className="app-root">
      <div className="app-container">
        <main className="app-main">
          {currentPage === 'selection' && (
            <SelectionPage
              activities={activities}
              selectedActivity={selectedActivity}
              handleActivitySelect={handleActivitySelect}
              numParticipants={numParticipants}
              setNumParticipants={setNumParticipants}
              handleStartEnrollment={handleStartEnrollment}
            />
          )}

          {currentPage === 'enrollment' && selectedActivity && (
            <EnrollmentPage
              selectedActivity={selectedActivity}
              numParticipants={numParticipants}
              onBack={() => setCurrentPage('selection')}
            />
          )}
        </main>

        <footer className="app-footer">
          <p>Trabajo Practico Numero 6 - ISW</p>
        </footer>
      </div>
    </div>
  );
};

export default App;
