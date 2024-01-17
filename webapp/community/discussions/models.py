from webapp import db
from datetime import datetime
from sqlalchemy.orm import relationship


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

    answers = relationship("Answers", backref="discussions", lazy="dynamic")

    def answer_count(self):
        return self.answers.count()

    def __repr__(self):
        return f"<ID: {self.id} Title{self.title}>"


class Answers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id", ondelete="CASCADE"),
        index=True
    )
    discussion_id = db.Column(
        db.Integer,
        db.ForeignKey("discussions.id", ondelete="CASCADE"),
        index=True
    )

    def __repr__(self):
        return f"ID:{self.id} USER_ID:{self.user_id} DISCUSSIONS_ID:{self.discussion_id}"