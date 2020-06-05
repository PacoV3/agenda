# Configuración del servidor de producción
from app import app # De la carpteta app trae el objeto app

# Para trabajar con la consola - base de datos
from app import db
from app.models import User, Contact

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Contact': Contact}
