#!/usr/bin/env python3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from sys_info import get_system_info
from sys_info import get_ip_address

battery, memory, cpu = get_system_info()
ip_adress = get_ip_address()

def send_email():
    smtp_server = "smtp-mail.outlook.com" # example for outlook email | change smtp server for your sender email account
    smtp_port = 587 
    smtp_username = "example@outlook.com" # change sender email username
    smtp_password = "" # put your sender email password

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        msg = MIMEMultipart()
        msg["From"] = "testingapp345@outlook.com" 
        msg["To"] = "pavel.vorop2004@gmail.com"
        msg["Subject"] = "PC is Turned On"
        message = f"Current IP Address: {ip_adress}\nBattery: {battery}%\nFree RAM Memory: {memory:.2f} MB\nCPU load: {cpu}%"
        msg.attach(MIMEText(message, "plain"))

        server.send_message(msg)
        print("Email successfully sent")

    except Exception as e:
        print("Error sending email:", e)

    finally:
        if 'server' in locals():
            server.quit()

if __name__ == "__main__":
    send_email()
