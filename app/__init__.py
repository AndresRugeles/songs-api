from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Inicializar la app

def create_app():
    app = Flask(__name__)

    # Configurar Limiter
    limiter = Limiter(
        key_func=get_remote_address, # Identifica al clinte por IP
        default_limits=["100 per hour"] # Límite global
    )
    limiter.init_app(app)
    
    from .routes import main
    app.register_blueprint(main)
    return app