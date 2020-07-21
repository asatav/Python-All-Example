import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from']="Arnav Satav"
email['to']="ashishsatav968@gmail.com"
email['subject']='Test email'

email.set_content(html.substitute({'name':'ASHISH'}),'html')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('arnavsatav13@gmail.com','Arnav@7577')
    smtp.send_message(email)
    print("All is GOOD!!!!")