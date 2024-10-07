import os


class Config:
    DEBUG = True

    SECRET_KEY = (
        os.environ.get("SECRET_KEY") or "shsuy3y9e8hhwa1i2#$@##4tlytyskb}{FG{}}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    JWT_SECRET_KEY = SECRET_KEY
    JWT_REFRESH_TOKEN_EXPIRES = 2600
    JWT_REFRESH_TOKEN_EXPIRES = 2592000
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ["access", "refresh"]
    REDIS_URL = os.environ.get("REDIS_URL")

    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = "noreply@example.com"
    MAIL_SERVER = ""
    MAIL_PORT = 587
