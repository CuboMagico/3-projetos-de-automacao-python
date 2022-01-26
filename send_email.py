import smtplib, ssl
from email.message import EmailMessage


subject = "Enviando um email com Python"
body = "<p>Esse é um email de teste</p>"

# Aqui é necessário colocar um email que permita o acesso por aplicativos menos seguros
# Logo abaixo, a senha de acesso para esse email
# receiver_email são os emails que receberão a mensagem

sender_email = ""
receiver_email = ""
password = ""

message = EmailMessage()

message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

html = f"""
<html>
<body>
    <h1>{subject}</h1>
    <p>{body}</p>
</body>
</html>
"""

message.add_alternative(html, subtype="html")

context = ssl.create_default_context()

print("Enviando o email... ", end="")

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server :
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Sucesso!")