import React from 'react';

const REQUIRES_SIZE = ['Tirolesa', 'Palestra'];

const ParticipantCard = ({ index, data, onChange, activity }) => {
  const requiresClothingSize = REQUIRES_SIZE.includes(activity);

  const handleChange = (e) => {
    const { name, value } = e.target;
    onChange(index, name, value);
  };

  return (
    <div className="participant-card">
      <h4 className="participant-card__title">Datos del Participante {index + 1}</h4>

      <div className="participant-card__grid">
        <label className="form-field">
          <span className="form-field__label">Nombre Completo:</span>
          <input
            type="text"
            name="nombre"
            value={data.nombre || ''}
            onChange={handleChange}
            required
            className="form-field__input"
          />
        </label>

        <label className="form-field">
          <span className="form-field__label">DNI (Documento):</span>
          <input
            type="text"
            name="dni"
            value={data.dni || ''}
            onChange={handleChange}
            required
            className="form-field__input"
          />
        </label>

        <label className="form-field">
          <span className="form-field__label">Edad:</span>
          <input
            type="number"
            name="edad"
            value={data.edad || ''}
            onChange={handleChange}
            min="1"
            required
            className="form-field__input"
          />
        </label>

        {requiresClothingSize && (
          <label className="form-field">
            <span className="form-field__label">Talle de Vestimenta (S, M, L, etc.):</span>
            <input
              type="text"
              name="talla"
              value={data.talla || ''}
              onChange={handleChange}
              required
              className="form-field__input"
            />
          </label>
        )}
      </div>
    </div>
  );
};

export default ParticipantCard;
