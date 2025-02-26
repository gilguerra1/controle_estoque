import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv


load_dotenv()

EMAIL_REMETENTE = os.getenv('EMAIL_REMETENTE')
SENHA_REMETENTE = os.getenv('SENHA_REMETENTE')
EMAIL_DESTINATARIO = os.getenv('EMAIL_DESTINATARIO')

def product_inventory_email(subject, message):

    msg = MIMEMultipart()
    msg['From'] = EMAIL_REMETENTE
    msg['To'] = EMAIL_DESTINATARIO
    msg['Subject'] = subject
    msg['Reply-To'] = EMAIL_REMETENTE

    msg.attach(MIMEText(message, 'html'))

    try: 

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(EMAIL_REMETENTE, SENHA_REMETENTE)
            server.send_message(msg)
        print('Email enviado com sucesso!')

    except Exception as e:
        print(f'Erro ao enviar email: {e}')
