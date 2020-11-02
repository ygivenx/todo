"""Database models for our application."""


# TODO: Write a model for your TODO tasks - it should contain at least:
# * body: text of the task
# * done: boolean value to mark task as done

from todo import db


class TODO(db.Model):
    """
    Define the TODO app model

    """

    __tablename__ = "todo"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    body = db.Column(db.String(100), default="")
    done = db.Column(db.Boolean, default=False)
