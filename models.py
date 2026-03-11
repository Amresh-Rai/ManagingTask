from datetime import datetime
from app import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    due_date = db.Column(db.Date, nullable=True)
    status = db.Column(db.String(20), nullable=False, default='Pending')
    remarks = db.Column(db.Text, nullable=True)
    created_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    last_updated_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    created_by_name = db.Column(db.String(100), nullable=False)
    created_by_id = db.Column(db.String(50), nullable=False)
    
    last_updated_by_name = db.Column(db.String(100), nullable=False)
    last_updated_by_id = db.Column(db.String(50), nullable=False)

    @property
    def created_by(self):
        return f"{self.created_by_name} ({self.created_by_id})"

    @property
    def last_updated_by(self):
        return f"{self.last_updated_by_name} ({self.last_updated_by_id})"
