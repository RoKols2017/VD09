class Config:
    SECRET_KEY = 'dev'  # будет переопределён в instance/config.py
    SQLALCHEMY_DATABASE_URI = 'sqlite:///clicker.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
