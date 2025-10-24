    import React, { useEffect, useMemo, useState } from 'react';
    import SelectionPage from './pages/SelectionPage';
    import EnrollmentPage from './pages/EnrollmentPage';
    import { getDisponibilidad } from './api';
    import './styles.css';

    const CUPOS = { Safari: 8, Tirolesa: 10, Palestra: 12, Jardinería: 12 };
    const ICONS = { Safari: '🦓', Palestra: '🧗', Tirolesa: '🦅', Jardinería: '🌱' };
    const DESCS = {
      Palestra: 'Desafía la gravedad en nuestros muros de escalada.',
      Safari: 'Recorre la reserva. ¡Apto para toda la familia!',
      Tirolesa: 'Deslízate a gran velocidad (requiere talle).',
      Jardinería: 'Conecta con la naturaleza aprendiendo sobre plantas.',
    };

    export default function App() {
      const [currentPage, setCurrentPage] = useState('selection'); // 'selection' | 'enrollment'
      const [selectedActivity, setSelectedActivity] = useState(null);
      const [numParticipants, setNumParticipants] = useState(1);
      const [loading, setLoading] = useState(true);
      const [activities, setActivities] = useState([]);

      // ---- carga y refresco de disponibilidad ----
      const loadDisponibilidad = async () => {
        const { items } = await getDisponibilidad();
        const enriched = items.map((it) => ({
          ...it,
          title: it.actividad,
          icon: ICONS[it.actividad] || '🌱',
          description: DESCS[it.actividad] || 'Conecta con la naturaleza aprendiendo sobre plantas.',
          cupoMax: CUPOS[it.actividad] || 12,
          turnos: [...it.turnos].sort((a, b) => a.hora.localeCompare(b.hora)),
        }));
        setActivities(enriched);
      };

      useEffect(() => {
        (async () => {
          try { await loadDisponibilidad(); }
          finally { setLoading(false); }
        })();
      }, []);

      // 🟢 OPCIONAL: “tiempo real” con polling cuando estás en Selección
      useEffect(() => {
        if (currentPage !== 'selection') return;
        const id = setInterval(() => { loadDisponibilidad(); }, 5000); // cada 5s
        return () => clearInterval(id);
      }, [currentPage]);

      const requiresSizeSet = useMemo(
        () => new Set(activities.filter(a => a.requiere_vestimenta).map(a => a.title)),
        [activities]
      );

      const goToSelectionAndRefresh = async () => {
        // refrescamos cupos y volvemos a la portada
        await loadDisponibilidad();
        setSelectedActivity(null);
        setCurrentPage('selection');
      };

      if (loading) {
        return <div className="app-root"><div className="app-container"><main className="app-main"><p>Cargando…</p></main></div></div>;
      }

      return (
        <div className="app-root">
          <div className="app-container">
            <main className="app-main">
              {currentPage === 'selection' && (
                <SelectionPage
                  activities={activities}
                  selectedActivity={selectedActivity}
                  handleActivitySelect={setSelectedActivity}
                  numParticipants={numParticipants}
                  setNumParticipants={setNumParticipants}
                  handleStartEnrollment={() => {
                    if (!selectedActivity) return alert('Selecciona una actividad.');
                    const ok = (selectedActivity.turnos || []).some(t => (t.cupo_disponible || 0) >= numParticipants);
                    if (!ok) return alert(`La actividad "${selectedActivity.title}" no tiene turnos con ${numParticipants} lugar(es).`);
                    setCurrentPage('enrollment');
                  }}
                />
              )}

              {currentPage === 'enrollment' && selectedActivity && (
                <EnrollmentPage
                  selectedActivity={selectedActivity}
                  numParticipants={numParticipants}
                  requiresSizeSet={requiresSizeSet}
                  onBack={async () => { await goToSelectionAndRefresh(); }}
                  // 🔑 callback que usaremos tras inscribir
                  onSuccess={async () => { await goToSelectionAndRefresh(); }}
                />
              )}
            </main>

            <footer className="app-footer">
              <p>Trabajo Práctico N° 6 - ISW</p>
            </footer>
          </div>
        </div>
      );
    }
