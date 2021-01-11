# we need to import a couple of classes.
# One to create email messages,
# and the other to connect to an SMTP server for sending emails.

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

message = MIMEMultipart()
message["from"] = "Tomas Carignano"
message["to"] = "sltctomas@gmail.com"
message["subject"] = "Testing"
message.attach(MIMEText("body"))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("sltctomas@gmail.com", "jajajaja")
    smtp.send_message(message)

print("Sent...")
