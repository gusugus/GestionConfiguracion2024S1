from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Crea una instancia de SQLAlchemy
db = SQLAlchemy()

# Elimina la creación del motor de la base de datos aquí

# Elimina la creación de la sesión SQLAlchemy aquí

# Define una función para obtener la sesión de la base de datos
def get_db_session():
    return db.session
