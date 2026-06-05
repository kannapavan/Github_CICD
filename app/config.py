import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")
    ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
    APP_VERSION = os.getenv("APP_VERSION", "0.1.0")
