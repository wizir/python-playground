from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import io
import smtplib

with io.open("config.txt") as f:
    lines = f.read().splitlines()

fromaddr = lines[2]
toaddress = lines[3]

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddress
msg['Subject'] = 'Python email'

body = 'Python text email'
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.mail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()

server.login(lines[0], lines[1])

text = msg.as_string()
server.sendmail(fromaddr, toaddress, text)