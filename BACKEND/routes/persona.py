from typing import Optional
from fastapi import APIRouter
from datetime import datetime
from pydantic import BaseModel

persona = APIRouter()
personas =[]

class listar_personas(BaseModel):
    id:str
    nombre:str
    primer_apellido:str
    segundo_apellido: Optional [str]
    edad:int
    fecha_nacimiento: datetime
    curp:str
    tipo_sangre:str
    fecha_creacion: datetime = datetime.now()
    estatus: bool = False


@persona.get("/personas")
def helloworld():
     return personas


@persona.get("/")
def Welcometoapi():
     return "Hola Mundo!"
 
@persona.post("/personas")
def enviarDatos(guardar_personas:listar_personas):
    personas.append(guardar_personas)
    {
           "id": "1",
    "nombre": "Marvin",
    "primer_apellido": "Tolentino",
    "segundo_apellido": "Perez",
    "edad": 20,
    "fecha_nacimiento": "2002-10-14T20:45:30.029000Z",
    "curp": "TOPM021014HPLLRRA",
    "tipo_sangre": "b+",
    "fecha_creacion": "2024-06-20T14:45:26.082373",
    "estatus": true
  },
    
    return "Datos Enviados"
