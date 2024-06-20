from fastapi import APIRouter

persona = APIRouter()
@persona.get("/personas")
def helloworld():
    return "Hola Mundo!"


@persona.get("/")
def Welcometoapi():
    return "Bienvenido a la api"