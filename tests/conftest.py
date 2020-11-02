__author__ = "Rohan Singh"

from flask import Flask
from pytest import fixture
from todo import db as _db


@fixture
def test_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    app.config["TESTING"] = True

    _db.init_app(app)

    with app.app_context():
        _db.create_all()
        yield app
        _db.drop_all()
