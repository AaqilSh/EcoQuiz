import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "ecoquizsecret")
    QUESTIONS_FILE = os.getenv("QUESTIONS_FILE", "questions.json")
    DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'
