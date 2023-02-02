from . import db
from datetime import datetime



# Create db model
class Servers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    ip = db.Column(db.String(12), nullable=False, unique=True)
    status = db.Column(db.String(12), nullable=False)
    status_date = db.Column(db.DateTime, default=datetime.now)
    date_created = db.Column(db.DateTime, default=datetime.now)
