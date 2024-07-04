import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.declarative import declarative_base

# Configuración básica de logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:1234@localhost/database_user"

engine = None
SessionLocal = None

try:
    # Crear el motor de SQLAlchemy con el URL de la base de datos
    engine = create_engine(SQLALCHEMY_DATABASE_URL)

    # Crear una sesión local con el motor
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    logger.info("Conexión a la base de datos establecida")
    
except OperationalError as e:
    logger.error(f"No se pudo establecer conexión a la base de datos: {e}")
    # Aquí podrías manejar la excepción según tus necesidades, por ejemplo, lanzando un error,
    # finalizando la aplicación, o realizando alguna acción de recuperación.

Base = declarative_base()
