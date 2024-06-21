from fastapi import FastAPI
from routes.persona import persona_router

app = FastAPI()

app.include_router(persona_router, prefix="/api")
