import os


CSRF_ENABLED = True
SECRET_KEY = os.urandom(32)

MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME', 'ian@example.com')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', 'password')