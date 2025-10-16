/**
 * Card horizontal para selección de actividad.
 */
const Card = ({ icon, title, description, isSelected, onClick }) => {
  return (
    <div
      className={`card ${isSelected ? 'card--selected' : 'card--unselected'}`}
      onClick={onClick}
      role="button"
      tabIndex={0}
      onKeyPress={(e) => { if (e.key === 'Enter') onClick(); }}
    >
      <div className="card__icon" aria-hidden>{icon}</div>

      <div className="card__body">
        <h3 className="card__title">{title}</h3>
        <p className="card__desc">{description}</p>
      </div>

      {isSelected && <div className="card__tag">SELECCIONADA</div>}
    </div>
  );
};

export default Card;
