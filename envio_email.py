from decouple import config
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_email(resultados):

    remetente = config("MEU_EMAIL")
    senha = config("MINHA_SENHA_EMAIL")
    destinatario = config("MEU_EMAIL")

    mensagem = MIMEMultipart()
    mensagem["From"] = remetente
    mensagem["To"] = destinatario
    mensagem["Subject"] = "Nenhum processo encontrado ainda 😑" if resultados == "Nenhum resultado encontrado" else "PROCESSO JUDICIAL ENCONTRADO! 🥳"

    agora = datetime.now()
    timestamp = agora.strftime("%d/%m/%Y")

    corpo = f"Olá,\n\nAqui está o resultado da consulta de {timestamp}:\n\n{resultados}\n\nAbraços!"
    mensagem.attach(MIMEText(corpo, "plain"))

    try:
        servidor = smtplib.SMTP("smtp.gmail.com", 587)
        servidor.starttls()
        servidor.login(remetente, senha)
        servidor.sendmail(remetente, destinatario, mensagem.as_string())
        servidor.quit()
        print("Email enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar email: {e}")