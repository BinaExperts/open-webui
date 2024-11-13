import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from . import const
from fastapi import HTTPException, status


class EmailService:
    def __init__(self, smtp_server, smtp_port, sender_email, sender_password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_email(self, recipient_email, subject, plain_message, html_message=None):
        try:
            # Create a MIME multipart email
            msg = MIMEMultipart("alternative")
            msg['From'] = self.sender_email
            msg['To'] = recipient_email
            msg['Subject'] = subject

            # Attach both plain text and HTML versions
            msg.attach(MIMEText(plain_message, 'plain'))
            if html_message:
                msg.attach(MIMEText(html_message, 'html'))

            # Send email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.sendmail(self.sender_email, recipient_email, msg.as_string())
            return True
        except Exception as e:
            print(f"Failed to send email: {e}")
            return False


class EmailConfirmation(EmailService):
    CONFIRMATION_EMAIL_TEMPLATE = const.CONFIRMATION_EMAIL_TEMPLATE

    def generate_confirmation_email(self, user_name, confirmation_link):
        # Read HTML template from file
        try:
            with open(self.CONFIRMATION_EMAIL_TEMPLATE, "r") as file:
                html_template = file.read()
        except FileNotFoundError:
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST, detail=const.FAILED_TO_GENERATE_CONFIRMATION_EMAIL
            )

        # Customize the HTML content
        html_message = html_template.format(user_name=user_name, confirmation_link=confirmation_link)

        # Plain text version
        plain_message = f"Hello {user_name}, please confirm your registration by clicking the link below:\n\n{confirmation_link}"

        return plain_message, html_message

    def send_confirmation(self, recipient_email, user_name, confirmation_link):
        subject = "Confirm Your Registration"
        plain_message, html_message = self.generate_confirmation_email(user_name, confirmation_link)

        if plain_message and html_message:
            return self.send_email(recipient_email, subject, plain_message, html_message)
        else:
            print("Failed to generate email content.")
            return False
