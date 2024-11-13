import os

CONFIRMATION_EMAIL_TEMPLATE = os.path.join(
    os.path.dirname(__file__),  # get the directory of the current file
    'apps', 'webui', 'binaexperts', 'assets', 'templates', 'confirmation_email.html'
)

FAILED_TO_GENERATE_CONFIRMATION_EMAIL = 'failed to generate the confirmation email'
