import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "jcxc4b@gmail.com"
password = "sxgr vjna tkds llxf"

receiver = "jcxc4b@gmail.com"
my_context = ssl.create_default_context()

message = """
Hey!
How have you been?
Wishing you the best!
"""

with smtplib.SMTP_SSL(host, port, context=my_context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)

