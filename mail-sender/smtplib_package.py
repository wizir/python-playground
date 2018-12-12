import smtplib
import io

# lines:
# email login
# email password
# sender address
# recipient address

with io.open('config.txt') as file:
    lines = file.read().splitlines()

server = smtplib.SMTP('smtp.mail.com', 587)

server.login(lines[0], lines[1])

msg = "Hello python!"

server.sendmail(lines[2], lines[3], msg, )