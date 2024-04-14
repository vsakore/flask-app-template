import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = "QWERTYQWERTYQWERTY"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
