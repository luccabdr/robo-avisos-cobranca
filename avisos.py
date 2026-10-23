import os
import smtplib
from datetime import date
from email.message import EmailMessage

import pandas as pd
from dotenv import load_dotenv

load_dotenv()
USUARIO = os.getenv("EMAIL_USUARIO")
SENHA = os.getenv("EMAIL_SENHA")

DIAS_AVISO = 3
MODO_TESTE = True  # True = todos os e-mails vão para o SEU endereço


def montar_email(c):
    primeiro = c["nome"].split()[0]
    data = c["vencimento"].strftime("%d/%m")
    valor = f"R$ {c['valor']:.2f}"
    if c["dias"] < 0:
        assunto = "Aviso de Cobrança"
        corpo = f"Olá, {primeiro}! Sua cobrança de {valor} venceu em {data} e está com {-c['dias']} dias de atraso. Qualquer dúvida ou esclarecimento, responda este e-mail!"
    else:
        assunto = "Lembrete de vencimento"
        corpo = f"Olá, {primeiro}! Sua cobrança de {valor} vence em {data}."
    return assunto, corpo


def enviar(smtp, destino, assunto, corpo):
    msg = EmailMessage()
    msg["From"] = USUARIO
    msg["To"] = destino
    msg["Subject"] = assunto
    msg.set_content(corpo)
    smtp.send_message(msg)


df = pd.read_excel("cobrancas.xlsx")
df["vencimento"] = pd.to_datetime(df["vencimento"]).dt.date
hoje = date.today()
df["dias"] = df["vencimento"].apply(lambda d: (d - hoje).days)

pagou = df["pago"].str.strip().str.lower() == "sim"
nao_pagas = df[~pagou]
avisar = nao_pagas[nao_pagas["dias"] <= DIAS_AVISO]

if not USUARIO or not SENHA:
    raise SystemExit("Faltam EMAIL_USUARIO e EMAIL_SENHA no arquivo .env")

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(USUARIO, SENHA)
    for _, c in avisar.iterrows():
        assunto, corpo = montar_email(c)
        if MODO_TESTE:
            destino = USUARIO
            assunto = f"[TESTE para {c['email']}] {assunto}"
        else:
            destino = c["email"]
        enviar(smtp, destino, assunto, corpo)
        print("Enviado para:", destino)