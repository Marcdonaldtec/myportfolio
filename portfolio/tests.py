from django.test import TestCase

# Create your tests here.
import os
import smtplib
from email.mime.text import MIMEText

# Récupérez les informations d'identification à partir des variables d'environnement
email = os.environ.get('SMTP_EMAIL')
password = os.environ.get('SMTP_PASSWORD')

server = None  # Initialisez la variable à None en dehors du bloc try

try:
    # Utiliser le port SSL au lieu de TLS
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(email, password)

    # Exemple d'envoi de courriel
    subject = 'Test Email'
    body = 'Ceci est un test email.'
    sender_email = email
    recipient_email = 'marcdomeus21@gmail.com'

    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = recipient_email

    server.sendmail(sender_email, [recipient_email], message.as_string())

    print("Email sent successfully.")
except Exception as e:
    print(f"Email sending failed: {type(e)} - {e}")
    import traceback
    traceback.print_exc()
finally:
    if server:
        server.quit()


