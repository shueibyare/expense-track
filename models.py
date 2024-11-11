import datetime
from email.policy import default

from application import db,app
from datetime import datetime

with app.app_context():
    db.create_all()


class IncomeExpenses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String, default="Income", nullable=False)
    category = db.Column(db.String, nullable=False)
    amount = db.Column(db.Integer, default="amount" ,nullable=False)
    total_amount = db.Column(db.Integer, nullable=False)
    remarks = db.Column(db.String, default="Add Remarks", nullable=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    __table_args__ = {'extend_existing': True}

    def __str__(self):
        return self.id
