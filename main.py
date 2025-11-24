import collections.abc
import collections

# --- INICIO DEL PARCHE DE COMPATIBILIDAD ---
# Python 3.10+ eliminó collections.Mapping, pero experta lo necesita.
# Esto agrega las referencias faltantes de nuevo a collections.
if not hasattr(collections, "Mapping"):
    collections.Mapping = collections.abc.Mapping
if not hasattr(collections, "MutableMapping"):
    collections.MutableMapping = collections.abc.MutableMapping
if not hasattr(collections, "Iterable"):
    collections.Iterable = collections.abc.Iterable
# --- FIN DEL PARCHE ---

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from controller_diagnostico import procesar_diagnostico
import uvicorn
import os

app = FastAPI(
    title='Diagnostico de Fallas en Motos API',
    description='Una API diseñada para recrear un SBC que diagnostique fallas comunes en motocicletas utilizando reglas basadas en síntomas proporcionados por el usuario.',
    version='1.0'
)

# app.include_router(routerMovie)
# app.include_router(routerUser)

# Base.metadata.create_all(bind=engine)


@app.get('/',tags=['Inicio'])
def read_root ():
    return HTMLResponse("<h1>API para el diagnostico de motos</h1>")

# Endpoint para el diagnóstico de fallas de motos, 
# Utilizando un sistema basado en reglas de conocimiento
@app.post('/diagnostico/inicial', tags=['Diagnostics'])
def diagnostico_inicial():
    # return {
    #     "type": "question",
    #     "text": "¿El freno de disco presenta alguno de los siguientes síntomas?",
    #     "options": ["Poca presión al frenar", "Ruidos al frenar","Vibraciones al frenar", "Ninguno"]
    # }
    return procesar_diagnostico(None)

@app.post('/diagnostico/responder', tags=['Diagnostics'])
def diagnostico_responder(data: dict):
    return procesar_diagnostico(data) 

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
