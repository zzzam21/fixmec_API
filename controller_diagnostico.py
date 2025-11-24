import collections.abc
import collections

# Parche necesario para Experta en Python 3.10+
if not hasattr(collections, "Mapping"):
    collections.Mapping = collections.abc.Mapping

from SBC.diagnostic_engine import Sintoma, DiagnosticoMoto

def procesar_diagnostico(respuestas):

    engine = DiagnosticoMoto()
    engine.reset()
    
    if not respuestas:
        engine.declare(Sintoma(diagnosis="inicial"))
        engine.run()
    else:
        inner = respuestas.get("respuestas", {})
        for key, value in inner.items():
            engine.declare(Sintoma(**{key: value}))
        engine.run()
        
    for fact in engine.facts.values():
        if 'pregunta' in fact:
            return {
                "type": "question",
                "key": fact['key'],   
                "text": fact['pregunta'],
                "options": fact['opciones']
            }
        elif 'diagnostico' in fact:
            return {
                "type": "diagnosis",
                "text": fact['diagnostico']
        }
    return {"type": "error", "text": "No se pudo determinar el diagnóstico."}
