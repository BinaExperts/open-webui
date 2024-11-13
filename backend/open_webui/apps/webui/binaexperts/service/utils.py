

def send_confirmation_email(email_service, user_email, user_name, confirmation_link):
    subject = "Confirm Your Registration"
    plain_message, html_message = generate_confirmation_email(user_name, confirmation_link)
    return email_service.send_email(user_email, subject, plain_message, html_message)
