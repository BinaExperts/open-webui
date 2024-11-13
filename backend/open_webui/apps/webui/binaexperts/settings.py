import os

SMTP_SERVER = str(os.environ.get("SMTP_SERVER", ""))
SMTP_PORT = str(os.environ.get("SMTP_PORT", ""))
SENDER_EMAIL = str(os.environ.get("SENDER_EMAIL", ""))
SENDER_PASSWORD = str(os.environ.get("SENDER_PASSWORD", ""))
