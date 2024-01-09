# app/__init__.py

from config             import Config
from flask              import Flask
from flask_sqlalchemy   import SQLAlchemy
from flask_migrate      import Migrate
from flask_login        import LoginManager
from flask_bootstrap    import Bootstrap


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'auth.login'
bootstrap = Bootstrap(app)



# Erstellen der Flask-Anwendung
def create_app(config_name='default'):
    
    # Laden der Konfiguration aus der Config-Klasse
    app.config.from_object(Config) 
    
    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .firm import firm as firm_blueprint
    app.register_blueprint(firm_blueprint)

    from .profil import profil as profil_blueprint
    app.register_blueprint(profil_blueprint)

    from .job import job as job_blueprint
    app.register_blueprint(job_blueprint)

    return app


from app.home import routes
from app      import models
