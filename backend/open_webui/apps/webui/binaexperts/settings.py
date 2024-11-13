import os

SMTP_SERVER = str(os.environ.get("SMTP_SERVER", "smtp.elasticemail.com"))
SMTP_PORT = str(os.environ.get("SMTP_PORT", "2525"))
SENDER_EMAIL = str(os.environ.get("SENDER_EMAIL", "chat@binaexperts.com"))
SENDER_PASSWORD = str(os.environ.get("SENDER_PASSWORD", "82F9E2F6AF18208C04F68986D537F9B1FA22"))
