from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Lead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())

    name = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    message = db.Column(db.Text)

    page = db.Column(db.String(200))
    ip = db.Column(db.String(64))
