import React, { useState } from 'react';

const REQUIRES_SIZE = ['Tirolesa', 'Palestra'];
const TALLE_OPCIONES = ['XS', 'S', 'M', 'L', 'XL', 'XXL'];
const DNI_REGEX = /^\d{7,8}$/;

const ParticipantCard = ({ index, data, onChange, activity }) => {
  const requiresClothingSize = REQUIRES_SIZE.includes(activity);
  const [errors, setErrors] = useState({});

  
  const handleChange = (e) => {
  const { name, value } = e.target;
  let newValue = value;

  
  if (name === 'dni') newValue = (newValue || '').replace(/\D/g, '');
  if (name === 'talla') newValue = (newValue || '').toUpperCase();

  onChange(index, name, newValue);

  
  validateField(name, newValue);
};


  const validateField = (name, value) => {
    let error = '';

    if (name === 'dni') {
      if (!value) error = 'El DNI es obligatorio.';
      else if (!DNI_REGEX.test(value)) error = 'Debe tener 7 u 8 dígitos numéricos.';
    }

    if (name === 'edad') {
      const n = Number(value);
      if (isNaN(n)) error = 'La edad debe ser un número.';
      else if (n < 1) error = 'La edad mínima es 1.';
      else if (n > 100) error = 'La edad máxima es 100.';
    }

    if (name === 'talla' && requiresClothingSize) {
      if (!value) error = 'Seleccione un talle.';
      else if (!TALLE_OPCIONES.includes(value.toUpperCase()))
        error = 'Talle inválido (XS, S, M, L, XL o XXL).';
    }

    setErrors((prev) => ({ ...prev, [name]: error }));
  };

  const handleBlur = (e) => {
    const { name, value } = e.target;
    validateField(name, value);
  };

  return (
    <div className="participant-card">
      <h4 className="participant-card__title">Datos del Participante {index + 1}</h4>

      <div className="participant-card__grid">
        {/* Nombre */}
        <label className="form-field">
          <span className="form-field__label">Nombre Completo:</span>
          <input
            type="text"
            name="nombre"
            value={data.nombre || ''}
            onChange={handleChange}
            required
            className="form-field__input"
            placeholder="Ej: Ana Pérez"
          />
        </label>

        {/* DNI */}
        <label className="form-field">
          <span className="form-field__label">DNI (Documento):</span>
          <input
            type="text"
            name="dni"
            value={data.dni || ''}
            onChange={handleChange}
            onBlur={handleBlur}
            required
            inputMode="numeric"
            placeholder="Solo números (7-8 dígitos)"
            className={`form-field__input ${errors.dni ? 'input--error' : ''}`}
          />
          {errors.dni && <small className="error-text">{errors.dni}</small>}
        </label>

        {/* Edad */}
        <label className="form-field">
          <span className="form-field__label">Edad:</span>
          <input
            type="number"
            name="edad"
            value={data.edad || ''}
            onChange={handleChange}
            onBlur={handleBlur}
            min="1"
            max="100"
            required
            placeholder="1 - 100"
            className={`form-field__input ${errors.edad ? 'input--error' : ''}`}
          />
          {errors.edad && <small className="error-text">{errors.edad}</small>}
        </label>

        {/* Talle */}
        {requiresClothingSize && (
          <label className="form-field">
            <span className="form-field__label">Talle de Vestimenta:</span>
            <select
              name="talla"
              value={data.talla || ''}
              onChange={handleChange}
              onBlur={handleBlur}
              required
              className={`form-field__input ${errors.talla ? 'input--error' : ''}`}
            >
              <option value="">-- Seleccione --</option>
              {TALLE_OPCIONES.map((t) => (
                <option key={t} value={t}>
                  {t}
                </option>
              ))}
            </select>
            {errors.talla && <small className="error-text">{errors.talla}</small>}
          </label>
        )}
      </div>
    </div>
  );
};

export default ParticipantCard;
