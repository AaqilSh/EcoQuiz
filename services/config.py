import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "ecoquizsecret")
    QUESTIONS_FILE = os.getenv("QUESTIONS_FILE", "questions.json")
    DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'

class DevelopmentConfig(Config):
    DEBUG = True

    
class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = os.getenv("SECRET_KEY")
    if not SECRET_KEY:
        raise ValueError("No SECRET_KEY found.")