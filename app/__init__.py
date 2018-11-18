from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from algoliasearch import algoliasearch


from app.errors import bp as errors_bp
from app.main import bp as main_bp
from app.articles import bp as articles_bp

db = SQLAlchemy()
migrate = Migrate()



# from app import routes
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    from app.models import db
    db.init_app(app)
    migrate.init_app(app, db)
    

    app.register_blueprint(main_bp)
    app.register_blueprint(errors_bp)
    app.register_blueprint(articles_bp)

    return app