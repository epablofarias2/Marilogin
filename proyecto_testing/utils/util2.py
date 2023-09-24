import os 
from dotenv import load_dotenv
from email.message import EmailMessage
import ssl
import smtplib
import random

def generar_codigo():
    codigo = random.randint(10000, 99999)
    return str(codigo)

def verificar_correo(correo_destino, mensaje):
    load_dotenv()
    email_sender = "codigoverificaciontesting@gmail.com"
    password = os.getenv("PASSWORD")

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = correo_destino
    em['Subject'] = "Código de verificación"
    em.set_content(mensaje)

    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(email_sender, password)
            smtp.sendmail(email_sender, correo_destino, em.as_string())
        print("Correo electrónico enviado correctamente")
    except Exception as e:
        print("Error al enviar el correo electrónico:", str(e))

