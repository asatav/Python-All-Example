# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC1c53eaf837b26e9ec579a6a959b3517a'
auth_token = 'c93fb1448169a112aea130570ddc6879'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Chatrapati shivaji maharaj ki jay..",
                     from_='+12026290153',
                     to='+919028259947'
                 )

print(message.sid)