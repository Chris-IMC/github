import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = input("Escribe el asunto y presiona enter: ")
body = input("Escribe el cuerpo y presiona enter: ")
sender_email = input("Escribe la direccion desde la que se enviara el correo y presiona enter: ")
receiver_email = input("Escribe la direccion de destino y presiona enter: ")
password = input("Escribe tu contraseña y presiona enter: ")

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email  

message.attach(MIMEText(body, "plain"))

filename = "meme.jpeg"  

with open(filename, "rb") as attachment:
    
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

encoders.encode_base64(part)

part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

message.attach(part)
text = message.as_string()

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)