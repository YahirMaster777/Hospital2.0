from fastapi import FastAPI
from routes.persona import persona_router
from routes.users import user_router

app = FastAPI()

app.include_router(persona_router,user_router, prefix="/api")
