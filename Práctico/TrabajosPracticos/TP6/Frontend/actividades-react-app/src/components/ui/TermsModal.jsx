import React, { useEffect, useRef, useState } from 'react';
import '../../styles.css'; // asegura que tengas los estilos del modal en styles.css

/**
 * TermsModal.jsx
 *
 * Muestra los términos y condiciones en un modal con scroll obligatorio.
 * - Si el contenido requiere scroll, el botón "Aceptar" queda deshabilitado hasta que
 *   el usuario scrollee hasta el final.
 * - Si el contenido NO requiere scroll (por ejemplo en pantallas grandes), el botón
 *   se habilita automáticamente.
 *
 * Props:
 * - onAccept: función llamada al aceptar (sin cerrar el modal).
 * - onClose: función para cerrar el modal.
 */
const TermsModal = ({ onAccept, onClose }) => {
  const [canAccept, setCanAccept] = useState(false);
  const termsRef = useRef(null);

  // Handler de scroll: habilita cuando llega al final
  const handleScroll = () => {
    const el = termsRef.current;
    if (!el) return;
    const { scrollTop, scrollHeight, clientHeight } = el;
    if (scrollTop + clientHeight >= scrollHeight - 8) {
      setCanAccept(true);
    }
  };

  // Al montarse y cada vez que cambie el tamaño del contenedor,
  // verificamos si el contenido necesita scroll. Si no necesita, habilitamos el botón.
  useEffect(() => {
    const el = termsRef.current;
    if (!el) return;

    const checkIfScrollable = () => {
      // Si el contenido cabe sin scrollear, permitimos aceptar directamente
      if (el.scrollHeight <= el.clientHeight + 2) {
        setCanAccept(true);
      } else {
        // Si requiere scroll, nos aseguramos de que esté deshabilitado hasta que el usuario baje.
        setCanAccept(false);
      }
    };

    // Chequeo inicial
    checkIfScrollable();

    // Re-check si el usuario redimensiona la ventana (p.ej. gira el celular)
    window.addEventListener('resize', checkIfScrollable);
    return () => window.removeEventListener('resize', checkIfScrollable);
  }, []);

  // Texto más extenso para forzar scroll en la mayoría de pantallas móviles
  const longTermsText = (
    <>
      <h3>TÉRMINOS Y CONDICIONES DE PARTICIPACIÓN</h3>

      <p>
        <strong>1. ACEPTACIÓN DE LOS TÉRMINOS</strong><br />
        Al utilizar esta aplicación y/o participar en las actividades ofrecidas, el usuario declara que ha leído,
        entendido y acepta estos términos y condiciones en su totalidad.
      </p>

      <p>
        <strong>2. REQUISITOS DE PARTICIPACIÓN</strong><br />
        El usuario se compromete a aportar información veraz y completa. Los organizadores se reservan el derecho
        de solicitar comprobantes o documentación adicional para validar la identidad o condiciones del participante.
      </p>

      <p>
        <strong>3. SALUD Y SEGURIDAD</strong><br />
        Las actividades pueden implicar riesgos físicos. Es responsabilidad del participante evaluar su propia
        capacidad física y consultar con un profesional de la salud si tiene dudas. El incumplimiento de normas de seguridad
        o el uso negligente de instalaciones exime de responsabilidad a los organizadores por incidentes derivados.
      </p>

      <p>
        <strong>4. CONDICIONES CLIMÁTICAS Y CANCELACIONES</strong><br />
        Por motivos de seguridad (clima adverso, fuerza mayor, incidentes técnicos) la organización podrá modificar
        o cancelar las actividades. En caso de cancelación se notificará a los inscritos por los canales disponibles
        y se indicarán las opciones (reprogramación, reembolso parcial o total, según política aplicable).
      </p>

      <p>
        <strong>5. DERECHOS Y OBLIGACIONES</strong><br />
        El participante se compromete a respetar las indicaciones del personal, el reglamento interno y las normas
        del parque/recinto. Queda prohibido causar daño intencional a instalaciones, flora, fauna o a otros participantes.
      </p>

      <p>
        <strong>6. USO DE IMÁGENES Y CONTENIDOS</strong><br />
        La organización podrá tomar fotografías o grabar material durante las actividades con fines de difusión.
        Si un participante se opone, deberá notificarlo por escrito antes del inicio de la actividad.
      </p>

      <p>
        <strong>7. TRATAMIENTO DE DATOS PERSONALES</strong><br />
        Los datos recopilados se utilizarán únicamente para la gestión de inscripciones, notificaciones y seguridad
        del evento. No se cederán a terceros sin el consentimiento explícito del titular, salvo obligación legal.
      </p>

      <p>
        <strong>8. LIMITACIÓN DE RESPONSABILIDAD</strong><br />
        En la máxima extensión permitida por la ley aplicable, la organización no será responsable por daños indirectos,
        incidentales o consecuentes derivados de la participación, salvo por dolo o negligencia grave.
      </p>

      <p>
        <strong>9. ACEPTACIÓN Y FIRMA ELECTRÓNICA</strong><br />
        Al presionar "Aceptar" el usuario manifiesta su conformidad y otorga su consentimiento electrónico, con plena
        validez jurídica para todos los efectos.
      </p>

      <p>
        <strong>10. DISPOSICIONES FINALES</strong><br />
        Estos términos se rigen por la legislación vigente en la jurisdicción correspondiente. Para cualquier disputa,
        las partes se someten a los tribunales competentes.
      </p>

      <p>
        <em>Por favor desliza hasta el final del contenido y presiona "Aceptar" para confirmar que leíste y entendiste estos términos.</em>
      </p>

      {/* Añadimos varios párrafos extra para asegurar longitud */}
      <p>
        INFORMACIÓN ADICIONAL: Los participantes con necesidades especiales o requerimientos particulares deberán comunicarlo
        previamente para que la organización pueda evaluar la posibilidad de adaptaciones.
      </p>

      <p>
        PROTOCOLOS: La organización podrá establecer protocolos temporales (p. ej. sanitarios). El incumplimiento de dichos
        protocolos puede resultar en la imposibilidad de participar sin derecho a reembolso.
      </p>

      <p>
        PROCEDIMIENTO DE RECLAMOS: Cualquier queja o reclamo deberá enviarse al correo oficial en el plazo establecido en la
        política de atención, adjuntando la documentación pertinente.
      </p>

      <p>
        POLÍTICA DE REEMBOLSOS: Los reembolsos, si aplican, se realizarán conforme a la política vigente en el momento de la
        compra/inscripción. Los gastos administrativos pueden ser retenidos según se estipule.
      </p>
    </>
  );

  return (
    <div className="modal-overlay">
      <div className="modal" role="dialog" aria-modal="true" aria-labelledby="terms-title">
        <h2 id="terms-title" style={{ textAlign: 'center' }}>Términos y Condiciones</h2>

        <div
          className="terms-content"
          ref={termsRef}
          onScroll={handleScroll}
          // añadir tabindex para que pueda scrollear con teclado si es necesario
          tabIndex={0}
        >
          {longTermsText}
        </div>

        <div className="modal-actions" style={{ alignItems: 'center' }}>
          <button onClick={onClose} className="btn btn--secondary">Cerrar</button>

          <button
            onClick={() => {
              if (!canAccept) return;
              onAccept();
            }}
            className="btn btn--primary"
            disabled={!canAccept}
            aria-disabled={!canAccept}
            style={{ marginLeft: 10 }}
          >
            Aceptar
          </button>
        </div>

        {!canAccept && (
          <small className="scroll-hint" style={{ display: 'block', marginTop: 8 }}>
            Desplázate hasta el final para habilitar el botón Aceptar
          </small>
        )}
      </div>
    </div>
  );
};

export default TermsModal;
