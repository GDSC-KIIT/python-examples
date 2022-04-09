# https://support.google.com/mail/answer/185833?hl=en

import smtplib
import ssl
import getpass

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "1905831@kiit.ac.in"  # Enter your address
receiver_email = "junaidrahim8d@gmail.com"  # Enter receiver address
password = getpass.getpass("Type your password and press enter: ")

message = """\
Subject: Hi there
This message is sent from Python. 
"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
