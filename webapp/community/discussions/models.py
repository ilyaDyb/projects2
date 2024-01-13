from webapp import db
from datetime import datetime


class Discussions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    autor = db.Column(
        db.Integer,
        db.ForeignKey("user.id", ondelete="CASCADE"),
        index=True
    )

    def __repr__(self):
        return f"<ID: {self.id} Title{self.title}>"