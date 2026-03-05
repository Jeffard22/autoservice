from flask import Flask
from dotenv import load_dotenv
import os
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Lead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    name = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    message = db.Column(db.Text)

    page = db.Column(db.String(200))
    ip = db.Column(db.String(64))

def create_app():
    load_dotenv()

    app = Flask(__name__)

    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-key")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///autoservice.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    with app.app_context():
        db.create_all()

    # routes
    from app.routes.main import main_bp
    app.register_blueprint(main_bp)

    return app
